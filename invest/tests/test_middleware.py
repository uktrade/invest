import pytest
from unittest.mock import patch, PropertyMock

from invest.helpers import IPStackAPIClient
from invest.middleware import GeoIPLanguageMiddleware, \
    LanguageAwareRedirectMiddleware, delocalise_path
from setup_guide.tests.factories import SetupGuidePageFactory

from . import factories


class DummyRequest:
    site = 1

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


@pytest.mark.parametrize(
    'language, expected_language',
    [
        ('en', 'en'),
        ('de', 'de'),
        ('foo', 'en')

    ])
def test_geoip_middleware(language, expected_language):
    with patch.object(IPStackAPIClient, 'get_language') as mock_get_language, \
         patch('invest.middleware.get_real_ip'):
        request = DummyRequest(language_code='en')
        mock_get_language.return_value = language
        response = GeoIPLanguageMiddleware(lambda x: x)(request=request)
        assert response.LANGUAGE_CODE == expected_language


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
