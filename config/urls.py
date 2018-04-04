from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.http import Http404
from django.contrib import admin
from django.views.generic import RedirectView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls

PREFIX_MAP = [
    # The original site put languages under /int but
    # it's more ergonomic to put them under the root.
    ('int/ar/', 'es/'),
    ('int/de/', 'de/'),
    ('int/es/', 'es/'),
    ('int/fr/', 'fr/'),
    ('int/ja/', 'jp/'),
    ('int/pt/', 'pt/'),
    # Django i18n splits Chinese into it's different
    # types, zh is directed to Simplified-Chinese
    ('int/zh/', 'zh-cn/'),
    # International landing pages;
    # Never implemented on the old site, they
    # duplicated the content.
    # Here they are directed to the correct language
    # page instead.
    ('cn/', 'zh-cn/'),  # Direct China to Simplified Chinese
    ('br/', 'pt/'),
    ('jp/', 'ja/'),
    # English language is default + not prefixed
    ('in/', ''),
    ('us/', ''),
    ('int/', ''),
]


class PrefixRedirect(RedirectView):
    """
    Redirect various prefixes from the old site into
    the new URL scheme.

    Where possible the new site keeps content under only
    one URL, where the old site often had the same content
    under different prefixes.
    """
    permanent = False

    PREFIX_MAP = PREFIX_MAP

    @classmethod
    def as_urls(cls):
        return '|'.join([prefix for prefix, mapping in cls.PREFIX_MAP])

    def get_redirect_url(self, *args, **kwargs):
        if hasattr(self.request, '__prefix_mapped__'):
            return False

        request = self.request
        path = request.path

        for prefix, mapping in PREFIX_MAP:
            if path.lstrip('/').startswith(prefix):
                request.__prefix_mapped__ = (prefix, mapping)
                path = request.path.replace(prefix, mapping, 1)
                request.path = path
                break
        else:
            return False

        # Only checks the directory part of the path in English -
        # Matching the behaviour on the invest.great.gov.uk site
        # where the pages were all in the same directories.
        path_components = [
            component for component in path.split('/') if component
        ]
        try:
            # Check validity by attempting to fetch page
            page, args, kwargs = \
                request.site.root_page.specific.route(request, path_components[1:])  # noqa

            return request.path
        except Http404:
            pass

        return False


urlpatterns = i18n_patterns(
    # redirect legacy urls
    url(PrefixRedirect.as_urls(), PrefixRedirect.as_view()),

    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    # url(r'^documents/', include(wagtaildocs_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
    prefix_default_language=False)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if settings.ENABLE_DEBUG_TOOLBAR:
        import debug_toolbar

        urlpatterns = [
                          url(r'^__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
