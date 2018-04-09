"""
Redirector that supports wagtail model translation

Based on info from -
https://github.com/infoportugal/wagtail-modeltranslation/issues/198#issuecomment-379772316
"""

from os.path import join

from .redirect import RedirectPrefixedPage
from modeltranslation import settings as mt_settings


class MTRedirectPrefixedPage(RedirectPrefixedPage):
    prefix_default_language = True

    def page_at(self, url):
        for language in mt_settings.AVAILABLE_LANGUAGES:
            if language != mt_settings.DEFAULT_LANGUAGE or self.prefix_default_language:
                url = url.lstrip('%s/' % language)

            page = super().page_at(self, url)
            if page is not None:
                return page