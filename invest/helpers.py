from django.conf import settings
import requests


class IPStackAPIClient:
    session = requests.Session()
    api_key = settings.IPSTACK_API_KEY
    base_url = 'http://api.ipstack.com/'
    auth = '?access_key=' + api_key

    @classmethod
    def get(cls, ip):
        url = cls.base_url + ip + cls.auth  # urljoin doesn't work with IPV6
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
        return ip_info.get('country_code', '')
