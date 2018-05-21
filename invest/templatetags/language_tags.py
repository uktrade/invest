import re

from django import template
from django.urls import resolve
from django.utils.translation import activate, get_language
from six import iteritems

register = template.Library()


@register.simple_tag(takes_context=True)
def change_lang_with_querystring(context, lang=None, *args, **kwargs):
    """Copied from wagtail-modeltranslation with the added ?lang=
    queryparam to set the cookie."""
    current_language = get_language()

    if 'request' in context and lang and current_language:
        request = context['request']
        match = resolve(request.path)
        non_prefixed_path = re.sub(
            current_language + '/', '', request.path, count=1
        )

        # means that is a wagtail page object
        if match.url_name == 'wagtail_serve':
            path_components = [component for component in
                               non_prefixed_path.split('/') if component]
            page, args, kwargs = request.site.root_page.specific.route(
                request, path_components
            )

            activate(lang)
            translated_url = page.url
            activate(current_language)
        elif match.url_name == 'wagtailsearch_search':
            path_components = [component for component in
                               non_prefixed_path.split('/') if component]

            translated_url = '/' + lang + '/' + path_components[0] + '/'
            if request.GET:
                translated_url += '?'
                for count, (key, value) in enumerate(iteritems(request.GET)):
                    if count != 0:
                        translated_url += "&"
                    translated_url += key + '=' + value
        if '?' in translated_url:
            translated_url += '&lang={lang}'.format(lang=lang)
        else:
            translated_url += '?lang={lang}'.format(lang=lang)
        return translated_url

    return ''
