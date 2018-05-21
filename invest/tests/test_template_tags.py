from unittest.mock import call, Mock, patch

import pytest

from invest.templatetags.language_tags import change_lang_with_querystring


@pytest.mark.parametrize(
    'change_lang_response,expected_response',
    [
        ('', ''),
        ('foo?bar=hello', 'foo?bar=hello&lang=es'),
        ('foo', 'foo?lang=es')
    ]
)
def test_change_lang_with_querystring(change_lang_response, expected_response):
    with patch(
            'invest.templatetags.language_tags.change_lang'
    ) as mocked_change_lang:
        context = Mock()
        mocked_change_lang.return_value = change_lang_response
        response = change_lang_with_querystring(context, 'es')
        assert response == expected_response
        assert mocked_change_lang.call_args == call(context, 'es')
