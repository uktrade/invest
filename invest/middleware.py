from collections import defaultdict

from django.http import HttpResponseRedirect
from django.utils import translation
from django.utils.translation import check_for_language
from ipware.ip import get_real_ip

from .helpers import IPStackAPIClient


COUNTRY_TO_LANGUAGE = defaultdict(lambda: 'en')
COUNTRY_TO_LANGUAGE.update(
    dict(
        CN='zh',  # China
        DE='de',  # Germany
        JP='jp',  # Japan
        FR='fr',  # France

        # Arabic speaking
        AE='ar',  # UAE
        SA='ar',  # Saudi Arabia

        # Portuguese speaking
        BR='pt',  # Brazil
        PT='pt',  # Portugal

        # English speaking
        GB='en',  # UK
        US='en',  # USA
        CA='en',  # Canada
        AU='en',  # Australia
        IN='en',  # India
        NZ='en',  # New Zealand

        # Spanish speaking
        ES='es',  # Spain
        MX='es',  # Mexico
        CO='es',  # Colombia
        AR='es',  # Argentina
        PE='es',  # Peru
        VE='es',  # Venezuela
        CL='es',  # Chile
        EC='es',  # Ecuador
        GT='es',  # Guatemala
        CU='es',  # Cuba
        HT='es',  # Haiti
        BO='es',  # Bolivia
        DO='es',  # Dominican Republic
        HN='es',  # Honduras
        PY='es',  # Paraguay
        NI='es',  # Nicaragua
        SV='es',  # El Salvador
        CR='es',  # Costa Rica
        PA='es',  # Panama
        PR='es',  # Puerto Rico
        UY='es',  # Uruguay
    )
)


class GeoIPLanguageMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = get_real_ip(request)
        if client_ip:
            country_code = IPStackAPIClient.get_country_code(client_ip)
            language = COUNTRY_TO_LANGUAGE[country_code]
            if check_for_language(language):
                request.LANGUAGE_CODE = language
                translation.activate(language)
                link = '/{lang}{path}'.format(
                    lang=language,
                    path=request.path
                )
                return HttpResponseRedirect(link)

        response = self.get_response(request)
        return response
