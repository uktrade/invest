import pytest
from unittest.mock import patch

from django.http import HttpResponsePermanentRedirect

from invest.helpers import IPStackAPIClient
from invest.middleware import GeoIPLanguageMiddleware
from setup_guide.tests.factories import SetupGuidePageFactory

from . import factories


class DummyRequest:
    LANGUAGE_CODE = 'en'


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
        request = DummyRequest()
        mock_get_language.return_value = language
        response = GeoIPLanguageMiddleware(lambda x: x)(request=request)
        assert response.LANGUAGE_CODE == expected_language


@pytest.mark.django_db
@pytest.mark.parametrize(
    'url, redirected_url',
    [
        ('/foo', '/foo-bar/'),
        ('/de/foo', '/de/foo-bar/'),
        ('/gh-gh/foo', '/gh-gh/foo-bar/')

    ])
def test_language_aware_redirect_middleware(url, redirected_url, client):
    page = SetupGuidePageFactory(
        path='/foo-bar'
    )
    factories.RedirectFactory(
        old_path='/foo/',
        redirect_page=page
    )
    response = client.get(url)
    assert response.status_code == 301
    import ipdb; ipdb.set_trace()
    assert response._headers['Location'] == redirected_url
