import pytest
from unittest.mock import patch, PropertyMock, call

from django.conf import settings

from invest.middleware import GeoIPLanguageMiddleware, \
    LanguageAwareRedirectMiddleware, LocaleQuerystringMiddleware, \
    delocalise_path
from setup_guide.tests.factories import SetupGuidePageFactory

from . import factories


class DummyRequest:
    site = 1
    session = {}
    GET = {}
    status_code = 200

    def __init__(self, path=None, language_code='en'):
        self.path = path
        self.language_code = language_code

    @property
    def LANGUAGE_CODE(self):
        return self.language_code

    @LANGUAGE_CODE.setter
    def LANGUAGE_CODE(self, value):
        self.language_code = value

    def get_full_path(self):
        return self.path


class DummyNotFoundResponse:
    status_code = 404


class DummyGoodResponse:
    status_code = 200


def test_locale_querystring_middleware_no_querystring():
    request = DummyRequest()
    LocaleQuerystringMiddleware(lambda x: DummyGoodResponse())(request=request)
    assert request.LANGUAGE_CODE == 'en'
    assert settings.LANGUAGE_SESSION_COOKIE_KEY not in request.session


def test_locale_querystring_middleware_sets_cookie():
    request = DummyRequest()
    request.GET['lang'] = 'es'
    LocaleQuerystringMiddleware(lambda x: DummyGoodResponse())(request=request)
    assert request.LANGUAGE_CODE == 'es'
    assert settings.LANGUAGE_SESSION_COOKIE_KEY in request.session
    assert request.session[settings.LANGUAGE_SESSION_COOKIE_KEY] == 'es'


@patch('invest.middleware.helpers.get_language_from_ip_address')
def test_geoip_language_cookie_not_set(mock_get_lang_from_ip):
    mock_get_lang_from_ip.return_value = 'es'
    request = DummyRequest()
    request.session = {}
    GeoIPLanguageMiddleware(lambda x: DummyGoodResponse())(request=request)
    assert request.LANGUAGE_CODE == 'es'
    assert mock_get_lang_from_ip.call_args == call(request)


@patch('invest.middleware.helpers.get_language_from_ip_address')
def test_geoip_language_cookie_set(mock_get_lang_from_ip):
    request = DummyRequest()
    request.session[settings.LANGUAGE_SESSION_COOKIE_KEY] = 'es'
    GeoIPLanguageMiddleware(lambda x: DummyGoodResponse())(request=request)
    assert mock_get_lang_from_ip.called is False


@patch('invest.middleware.helpers.get_language_from_ip_address')
def test_geoip_language_not_200_request(mock_get_lang_from_ip):
    request = DummyRequest()
    GeoIPLanguageMiddleware(lambda x: DummyNotFoundResponse())(request=request)
    assert mock_get_lang_from_ip.called is False


@pytest.mark.django_db
@pytest.mark.parametrize(
    'language_code, url, redirected_url',
    [
        ('en', '/foo', '/foo-bar/'),
        ('de', '/de/foo', '/de/foo-bar/'),
        ('gh-gh', '/gh-gh/foo', '/gh-gh/foo-bar/')

    ])
def test_language_aware_redirect_middleware(
        language_code, url, redirected_url):
    page = SetupGuidePageFactory(
        slug_en='foo-bar'
    )
    factories.RedirectFactory(
        old_path='/foo',
        redirect_page=page
    )
    request = DummyRequest(
        language_code=language_code,
        path=url
    )
    with patch(
            'wagtail.contrib.redirects.models.Redirect.link',
            new_callable=PropertyMock
    ) as mocked_link:
        mocked_link.return_value = redirected_url
        response = LanguageAwareRedirectMiddleware(
            lambda x: DummyNotFoundResponse())(request=request)
        assert response.status_code == 301
        assert response.url == redirected_url


@pytest.mark.django_db
def test_language_aware_redirect_middleware_200_response_no_redirect():
    page = SetupGuidePageFactory(
        slug_en='foo-bar'
    )
    factories.RedirectFactory(
        old_path='/foo',
        redirect_page=page
    )
    request = DummyRequest(
        language_code='en',
        path='foo'
    )
    incoming_response = DummyGoodResponse()
    response = LanguageAwareRedirectMiddleware(
            lambda x: incoming_response)(request=request)
    assert response == incoming_response


@pytest.mark.parametrize(
    'language_code, path, expected_path',
    [
        ('en', '/foo', '/foo'),
        ('de', '/de/foo', '/foo'),
        ('gh-gh', '/gh-gh/foo', '/foo')

    ])
def test_delocalise_path(language_code, path, expected_path):
    request = DummyRequest(
        language_code=language_code,
        path=path
    )

    assert delocalise_path(path, request) == expected_path
