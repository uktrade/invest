from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from config.redirect_mt import MTRedirectPrefixedPage, redirect_page_index_html
from config.settings import PREFIX_DEFAULT_LANGUAGE


class RedirectLanguagePrefixes(MTRedirectPrefixedPage):
    prefix_default_language = settings.PREFIX_DEFAULT_LANGUAGE
    prefix_map = [
        # The original site put languages under /int but
        # it's more ergonomic to put them under the root.
        ('int/ar/', 'ar/'),
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


urlpatterns = i18n_patterns(
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    # Redirects, for compatibility with the old site - redirect
    url(RedirectLanguagePrefixes.as_urls(),
        RedirectLanguagePrefixes.as_view()),
    url(r'', include(wagtail_urls)),

    url(r'index\.html$', redirect_page_index_html),
    prefix_default_language=PREFIX_DEFAULT_LANGUAGE)

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
