from urllib.parse import urljoin
from django.conf import settings
import requests


class IPStackAPIClient:
    session = requests.Session()
    api_key = settings.IPSTACK_API_KEY
    base_url = 'http://api.ipstack.com'
    auth = '?access_key=' + api_key
    endpoints = {
        'check': 'check'
    }

    @classmethod
    def get(cls, url_path):
        url = urljoin(cls.base_url, url_path) + cls.auth
        response = cls.session.get(url)
        data = response.json()
        if hasattr(data, 'error'):
            return None
        return data

    @classmethod
    def get_ip_info(cls):
        url = cls.endpoints['check']
        return cls.get(url)

    @classmethod
    def get_language(cls):
        ip_info = cls.get_ip_info()
        language = ip_info['location']['languages'][0]['code']
        return language
