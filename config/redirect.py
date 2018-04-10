from django.http import Http404
from django.views.generic import RedirectView


class RedirectPrefixes(RedirectView):
    """
    Redirect urls that start with particular strings

    Superclasses have an attribute named prefix_map
    containing the src and destination mappings.

    >>> class ExampleRedirector(RedirectPrefixes):
    >>>     prefix_map = [('planets/pluto','dwarf-planets/pluto')]
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'prefix_map'):
            raise AttributeError("%s has no prefix_map attribute")
        return super(RedirectPrefixes, cls).__new__(cls, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        """
        :return: new path if a known prefix or False
        """
        request = self.request
        if request.path is None:
            return

        path = request.path.lstrip('/')
        for prefix, mapping in self.prefix_map:
            if path.startswith(prefix):
                request.__prefix_mapped__ = (prefix, mapping)
                request.path = '/%s' % \
                               path.replace(prefix, mapping, 1).lstrip('/')
                break

        return request.path

    @classmethod
    def as_urls(cls):
        """
        :return:  regex pattern for use in urls.py
        """
        return '|'.join([prefix for prefix, mapping in cls.prefix_map])


def page_at(request, path):
    """
    :param path:
    :return:  Page at path
    """
    # Only checks the directory part of the path in English -
    # Matching the behaviour on the invest.great.gov.uk site
    # where the pages were all in the same directories.
    path_components = [
        component for component in path.split('/') if component
    ]

    try:
        # Check validity by attempting to fetch page
        page, args, kwargs = \
            request.site.root_page.specific.route(request, path_components)  # noqa

        return page
    except Http404:
        pass

    return None


class RedirectPrefixedPage(RedirectPrefixes):
    """
    Extend RedirectPrefix to redirect if a Page
    exists.
    """
    def get_redirect_url(self, *args, **kwargs):
        _path = self.request.path

        # get_redirect_url can modify request.path
        # so keep a copy
        path = super().get_redirect_url(self, *args, **kwargs)

        if path.startswith('//'):
            path = path[1:]

        page = page_at(self.request, path.lstrip('/'))
        if page is not None:
            if page.url is None:
                return path
            else:
                return page.url
        else:
            self.request.path = _path
            raise Http404()
