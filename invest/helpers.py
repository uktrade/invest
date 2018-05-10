from collections import defaultdict
from urllib.parse import urljoin

import requests
from django.conf import settings
from django.utils import translation
from ipware.ip import get_real_ip

COUNTRY_TO_LANGUAGE = defaultdict(lambda: settings.LANGUAGE_CODE)
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


class IPStackAPIClient:
    session = requests.Session()
    api_key = settings.IPSTACK_API_KEY
    base_url = 'http://api.ipstack.com'
    auth = '?access_key=' + api_key

    @classmethod
    def get(cls, ip):
        url = urljoin(cls.base_url, ip) + cls.auth
        response = cls.session.get(url)
        if response.ok:
            data = response.json()
            return data
        return {}

    @classmethod
    def get_ip_info(cls, ip):
        return cls.get(ip)

    @classmethod
    def get_language(cls, ip):
        ip_info = cls.get_ip_info(ip)
        if ip_info.get('location'):
            return ip_info['location']['languages'][0]['code']
        else:
            return None

    @classmethod
    def get_country_code(cls, ip):
        ip_info = cls.get_ip_info(ip)
        return ip_info.get('country_code')


def get_language_from_querystring(request):
    language_code = request.GET.get('lang')
    if translation.check_for_language(language_code):
        return language_code


def get_language_from_ip_address(request):
    client_ip = get_real_ip(request)
    if client_ip:
        country_code = IPStackAPIClient.get_country_code(client_ip)
        language_code = COUNTRY_TO_LANGUAGE[country_code]
        if translation.check_for_language(language_code):
            return language_code
    return settings.LANGUAGE_CODE
