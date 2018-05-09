import pytest


@pytest.mark.django_db
def test_request(client):

    client.get('/?utm_source=test_source&utm_medium=test_medium&utm_campaign=test_campaign&utm_term=test_term&utm_content=test_content')  # noqa

    correct_utm = {
        'utm_source': 'test_source',
        'utm_medium': 'test_medium',
        'utm_campaign': 'test_campaign',
        'utm_term': 'test_term',
        'utm_content': 'test_content'
    }

    assert 'utm' in client.session
    assert client.session['utm'] == correct_utm
