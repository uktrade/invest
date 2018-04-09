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
        path = request.path.lstrip('/')

        for prefix, mapping in self.prefix_map:
            if path.startswith(prefix):
                request.__prefix_mapped__ = (prefix, mapping)
                request.path = request.path.replace(prefix, mapping, 1)
                return request.path
        else:
            return path

    @classmethod
    def as_urls(cls):
        """
        :return:  regex pattern for use in urls.py
        """
        return '|'.join([prefix for prefix, mapping in cls.prefix_map])


class RedirectPrefixedPage(RedirectPrefixes):
    """
    Extend RedirectPrefix to redirect if a Page
    exists.
    """
    def page_exists(self, path):
        # Only checks the directory part of the path in English -
        # Matching the behaviour on the invest.great.gov.uk site
        # where the pages were all in the same directories.
        path_components = [
            component for component in path.split('/') if component
        ]
        try:
            # Check validity by attempting to fetch page
            request = self.request
            page, args, kwargs = \
                request.site.root_page.specific.route(request, path_components)  # noqa

            return True
        except Http404:
            pass

        return False

    def get_redirect_url(self, *args, **kwargs):
        _path = self.request.path

        # get_redirect_url modifies request.path
        # so keep a copy
        path = super().get_redirect_url(self, *args, **kwargs)

        if path.startswith('//'):
            path = path[1:]

        if self.page_exists(path):
            self.request.path = path
            return path
        else:
            self.request.path = _path
            raise Http404()
