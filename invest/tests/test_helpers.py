from unittest.mock import patch, Mock

import pytest

from invest.helpers import IPStackAPIClient, get_language_from_ip_address


@patch.object(IPStackAPIClient, 'session')
def test_ipstack_get_ip(mocked_session):
    mocked_response = Mock()
    mocked_response.ok = True
    mocked_response.json.return_value = {
        'ip': '134.201.250.155',
        'type': 'ipv4',
        'location': {
            'geoname_id': 5358705,
            'capital': 'Washington D.C.',
            'languages': [
                {
                    'code': 'en',
                    'name': 'English',
                    'native': 'English'
                }
            ],
        }
    }
    mocked_session.get.return_value = mocked_response
    language = IPStackAPIClient.get_language('128.0.0.1')
    assert language == 'en'


@patch.object(IPStackAPIClient, 'session')
def test_ipstack_error(mocked_session):
    mocked_response = Mock()
    mocked_response.ok = True
    mocked_response.json.return_value = {
        'error': {
            'code': 104,
            'type': 'monthly_limit_reached',
            'info': 'Your monthly API request volume has been reached. '
                    'Please upgrade your plan.'
        }
    }
    mocked_session.get.return_value = mocked_response
    language = IPStackAPIClient.get_language('128.0.0.1')
    assert language is None


@patch.object(IPStackAPIClient, 'session')
def test_ipstack_500(mocked_session):
    mocked_response = Mock()
    mocked_response.ok = False
    mocked_session.get.return_value = mocked_response
    language = IPStackAPIClient.get_language('128.0.0.1')
    assert language is None


@pytest.mark.parametrize(
    'returned_country_code,expected_language',
    [
        ('CN', 'zh'),
        ('DE', 'de'),
        ('JP', 'ja'),
        ('FR', 'fr'),
        ('AE', 'ar'),
        ('SA', 'ar'),
        ('BR', 'pt'),
        ('PT', 'pt'),
        ('GB', 'en'),
        ('US', 'en'),
        ('CA', 'en'),
        ('AU', 'en'),
        ('IN', 'en'),
        ('NZ', 'en'),
        ('ES', 'es'),
        ('MX', 'es'),
        ('CO', 'es'),
        ('AR', 'es'),
        ('PE', 'es'),
        ('VE', 'es'),
        ('CL', 'es'),
        ('EC', 'es'),
        ('GT', 'es'),
        ('CU', 'es'),
        ('HT', 'es'),
        ('BO', 'es'),
        ('DO', 'es'),
        ('HN', 'es'),
        ('PY', 'es'),
        ('NI', 'es'),
        ('SV', 'es'),
        ('CR', 'es'),
        ('PA', 'es'),
        ('PR', 'es'),
        ('UY', 'es'),
        ('PL', 'en')
    ],
    ids=(
        'China',
        'Germany',
        'Japan',
        'France',
        'UAE',
        'Saudi Arabia',
        'Brasil',
        'Portugal',
        'UK',
        'USA',
        'Canada',
        'Australia',
        'India',
        'New Zeland',
        'Spain',
        'Mexico',
        'Colombia',
        'Argentina',
        'Peru',
        'Venezuela',
        'Chile',
        'Ecuador',
        'Guatemala',
        'Cuba',
        'Haiti',
        'Bolivia',
        'Dominican Republic',
        'Honduras',
        'Paragua',
        'Nicaragua',
        'El Salvador',
        'Costa Rica',
        'Panama',
        'Puerto Rico',
        'Uruguay',
        'Poland'
    )
)
def test_language_from_ip(returned_country_code, expected_language):
    with patch(
            'invest.helpers.IPStackAPIClient.get_country_code'
    ) as mocked_get_country_code, patch('invest.helpers.get_real_ip'):
        mocked_get_country_code.return_value = returned_country_code
        assert get_language_from_ip_address(None) == expected_language
