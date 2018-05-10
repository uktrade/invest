from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import translation

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
        return settings.LANGUAGE_COOKIE_KEY in request.session

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
        request.session[settings.LANGUAGE_COOKIE_KEY] = language_code

    def __call__(self, request):
        language_code = helpers.get_language_from_querystring(request)
        if language_code:
            self.set_language_cookie(request, language_code)
            self.set_language_and_redirect(request, language_code)

        response = self.get_response(request)
        return response
