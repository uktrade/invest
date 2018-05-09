from django.utils import translation
from django.utils.translation import check_for_language
from ipware.ip import get_real_ip

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
