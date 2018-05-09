import pytest
from unittest.mock import patch

from invest.helpers import IPStackAPIClient
from invest.middleware import GeoIPLanguageMiddleware


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
