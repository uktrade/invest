"""
Redirector that supports wagtail model translation

Based on info from -
https://github.com/infoportugal/wagtail-modeltranslation/issues/198#issuecomment-379772316
"""
from django.http import Http404, HttpResponseRedirect

from .redirect import page_at, RedirectPrefixes
from modeltranslation import settings as mt_settings


def iter_language_prefixes(prefix_default_language=False):
    """
    yield: prefix, language
    """
    for language in mt_settings.AVAILABLE_LANGUAGES:
        if language != mt_settings.DEFAULT_LANGUAGE or \
                prefix_default_language:
            yield language, language
        else:
            yield '', language


def path_language_prefix(path):
    for prefix, language in iter_language_prefixes():
        if prefix and path.startswith('/%s/' % prefix):
            return prefix
    else:
        return ''


def path_language(path):
    lang = path_language_prefix(path)
    if not lang:
        return mt_settings.DEFAULT_LANGUAGE


def unprefix_path(path):
    if path[-1] != '/':
        path += '/'
    return path.lstrip('/%s' % path_language_prefix(path))


class MTRedirectPrefixedPage(RedirectPrefixes):
    """
    :attribute: raise_404 raise Http404 if no page found.

    Depening on url setup user may not wish to raise 404
    Raising a 404 will prevent other views from seeing
    the urls.

    Setting to False is useful if there are other views
    to handle defaults.
    """
    raise_404 = True
    prefix_default_language = True

    def get_redirect_url(self, *args, **kwargs):
        original_path = self.request.path
        path = super().get_redirect_url(self, *args, **kwargs)
        if path is None:
            path = original_path

        page = page_at(self.request, path)
        if page:
            return '/%s' % page.url.rstrip('/')
        else:
            page = page_at(self.request, unprefix_path(path))
            if page is not None:
                return path
            else:
                self.request.path = original_path
                if self.raise_404:
                    raise Http404()


def redirect_page_index_html(request):
    path = request.path.rstrip('/index.html')
    for page in (
            page_at(request, path), page_at(request, unprefix_path(path))
    ):
        if page is not None and page.url:
            return HttpResponseRedirect(page.url)

    raise Http404()
