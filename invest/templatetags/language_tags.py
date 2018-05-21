from django import template
from wagtail_modeltranslation.templatetags.wagtail_modeltranslation import \
    change_lang

register = template.Library()


@register.simple_tag(takes_context=True)
def change_lang_with_querystring(context, lang=None, *args, **kwargs):
    """Extend change_lang to add ?lang= queryparam to set the cookie."""

    translated_url = change_lang(context, lang, *args, **kwargs)
    if translated_url:
        if '?' in translated_url:
            translated_url += '&lang={lang}'.format(lang=lang)
        else:
            translated_url += '?lang={lang}'.format(lang=lang)
    return translated_url
