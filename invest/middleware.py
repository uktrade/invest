from urllib.parse import urlparse

from django import http
from django.conf import settings

from django.http import HttpResponseRedirect
from django.utils import translation
from django.utils.encoding import uri_to_iri
from wagtail.contrib.redirects import models

from . import helpers


class SetLanguageAndRedirectMixin:

    @staticmethod
    def get_language_code(request):
        raise NotImplemented

    @staticmethod
    def set_language_and_redirect(request, language_code):
        translation.activate(language_code)
        request.LANGUAGE_CODE = translation.get_language()
        link = '/{lang}{path}'.format(
            lang=language_code,
            path=request.path
        )
        return HttpResponseRedirect(link)


class GeoIPLanguageMiddleware(SetLanguageAndRedirectMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_language_code(request):
        return helpers.get_language_from_ip_address(request)

    @staticmethod
    def is_language_cookie_set(request):
        return settings.LANGUAGE_SESSION_COOKIE_KEY in request.session

    def __call__(self, request):
        language_code = self.get_language_code(request)
        if language_code and not self.is_language_cookie_set(request):
            self.set_language_and_redirect(request, language_code)

        response = self.get_response(request)
        return response


class LocaleQuerystringMiddleware(SetLanguageAndRedirectMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_language_code(request):
        return helpers.get_language_from_querystring(request)

    @staticmethod
    def set_language_cookie(request, language_code):
        request.session[settings.LANGUAGE_SESSION_COOKIE_KEY] = language_code

    def __call__(self, request):
        language_code = helpers.get_language_from_querystring(request)
        if language_code:
            self.set_language_cookie(request, language_code)
            self.set_language_and_redirect(request, language_code)

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
