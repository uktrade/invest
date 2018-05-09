from unittest.mock import patch, Mock

from invest.helpers import IPStackAPIClient


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
