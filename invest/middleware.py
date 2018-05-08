from modeltranslation import settings as mt_settings
from ipware.ip import get_real_ip

from .helpers import IPStackAPIClient


class GeoIPLanguageMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = get_real_ip(request)
        if client_ip:
            language = IPStackAPIClient().get_language(client_ip)
            if language in mt_settings.AVAILABLE_LANGUAGES:
                request.LANGUAGE_CODE = language

        response = self.get_response(request)
        return response
