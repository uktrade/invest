import sys

import ansicolor
import lxml
import re

from django.core.management.base import BaseCommand
from django.conf import settings
from django.urls import resolve, Resolver404
from urllib.parse import urlsplit  # Python 3

IGNORE_PATHS = [re.compile(rule) for rule in getattr(settings, 'CHECK_SITEMAP_IGNORE', [])]


class Command(BaseCommand):
    def parse_sitemap_urls(self, xml_root):
        """
        :param xml_root:  etree root of xml
        :return: urls
        """
        urls = xml_root.xpath(
            './/sitemap:loc/text()',
            namespaces={
                'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9',
            }
        )
        return urls

    def sitemap_urls(self, filename=settings.CHECK_SITEMAP):
        """
        Read sitemap xml and return urls
        :param filename:
        :return:
        """
        tree = lxml.etree.parse(filename)
        root = tree.getroot()
        urls = self.parse_sitemap_urls(root)
        return urls

    def check_url(self, url):
        """
        :param url:
        :return:  True if the url has a resolver
        """
        parsed = urlsplit(url)
        try:
            result = resolve(parsed.path)
            return parsed.path, True, result, None
        except Resolver404 as ex:
            return parsed.path, False, None, ex

    def url_status_msg(self, path, success, result, ex):
        return " ".join([ansicolor.green("✓ ") if success else ansicolor.red("✕ "), path])

    def should_ignore_path(self, url):
        for rule in IGNORE_PATHS:
            if re.match(rule, url):
                return True
        return False

    def urls_status(self, urls):
        for url in urls:
            path, success, result, ex = self.check_url(url)
            success = success or self.should_ignore_path(path)
            msg = self.url_status_msg(path, success, result, ex)
            yield success, msg

    def check_urls(self, urls):
        """
        Check if urls can be resolved

        Outputs messages showing which urls were resolved.
        Successful urls are output first, then failed urls
        this is better for the users, since there are
        usually less failures.

        :param   urls:  urls to check
        :return:  False if any urls could not be resolved
        """
        failed = []
        for success, msg in self.urls_status(urls):
            if success:
                self.stdout.write(msg)
            else:
                failed.append(msg)
        for msg in failed:
            self.stdout.write(msg)
        return not failed

    def handle(self, *args, **options):
        urls = self.sitemap_urls(settings.CHECK_SITEMAP)
        exit_code = 0 if self.check_urls(urls) else 1
        sys.exit(exit_code)
