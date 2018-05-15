from urllib.parse import urlparse

from django import http
from django.conf import settings
from django.utils import translation
from django.utils.encoding import uri_to_iri
from django.utils.translation import check_for_language
from ipware.ip import get_real_ip
from wagtail.contrib.redirects import models

from .helpers import IPStackAPIClient


class GeoIPLanguageMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = get_real_ip(request)
        if client_ip:
            language = IPStackAPIClient.get_language(client_ip)
            if check_for_language(language):
                request.LANGUAGE_CODE = language
                translation.activate(language)

        response = self.get_response(request)
        return response


def delocalise_path(path, request):
    lang = request.LANGUAGE_CODE
    if lang and lang != settings.LANGUAGE_CODE:  # exclude en
        lang_string = '/{lang}'.format(lang=lang)
        if path.startswith(lang_string):
            return path.replace(lang_string, '')
    return path


def _get_redirect(request, path):
    path = delocalise_path(path, request)
    try:
        return models.Redirect.get_for_site(request.site).get(old_path=path)
    except models.Redirect.MultipleObjectsReturned:
        # We have a site-specific and a site-ambivalent redirect;
        # prefer the specific one
        return models.Redirect.objects.get(site=request.site, old_path=path)
    except models.Redirect.DoesNotExist:
        return None


def get_redirect(request, path):
    redirect = _get_redirect(request, path)
    if not redirect:
        # try unencoding the path
        redirect = _get_redirect(request, uri_to_iri(path))
    return redirect


class LanguageAwareRedirectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # No need to check for a redirect for non-404 responses.
        response = self.get_response(request)

        if response.status_code != 404:
            return response

        # If a middleware before `SiteMiddleware` returned a response the
        # `site` attribute was never set, ref #2120
        if not hasattr(request, 'site'):
            return response

        # Get the path
        path = models.Redirect.normalise_path(request.get_full_path())

        # Find redirect
        redirect = get_redirect(request, path)
        import ipdb; ipdb.set_trace()
        if redirect is None:
            # Get the path without the query string or params
            path_without_query = urlparse(path).path

            if path == path_without_query:
                # don't try again if we know we will get the same response
                return response

            redirect = get_redirect(request, path_without_query)
            if redirect is None:
                return response

        if redirect.is_permanent:
            return http.HttpResponsePermanentRedirect(redirect.link)
        else:
            return http.HttpResponseRedirect(redirect.link)