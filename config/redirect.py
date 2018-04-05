from django.http import Http404
from django.views.generic import RedirectView


class RedirectPrefix(RedirectView):
    """
    Redirect urls that start with particular strings

    Superclasses have an attribute named prefix_map
    containing the src and destination mappings.

    >>> class ExampleRedirector(RedirectPrefixes):
    >>>     prefix_map = [('/planets/pluto','/dwarf-planets/pluto')]

    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'prefix_map'):
            raise AttributeError("%s has no prefix_map attribute")
        return cls

    def get_redirect_url(self, *args, **kwargs):
        """
        :return: new path if a known prefix or False
        """
        request = self.request
        path = request.path

        for prefix, mapping in PREFIX_MAP:
            if path.lstrip('/').startswith(prefix):
                request.__prefix_mapped__ = (prefix, mapping)
                request.path = request.path.replace(prefix, mapping, 1)
                return request.path
        else:
            return False

    @classmethod
    def as_urls(cls):
        """
        :return:  regex pattern for use in urls.py
        """
        return '|'.join([prefix for prefix, mapping in cls.prefix_map])


class RedirectPrefixedPage(RedirectPrefix):
    """
    Extend RedirectPrefix to redirect if a Page
    exists.
    """
    def get_redirect_url(self, *args, **kwargs):
        path = super().get_redirect_url(*args, **kwargs)
        if path is False:
            return False

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
                request.site.root_page.specific.route(request, path_components[1:])  # noqa

            return request.path
        except Http404:
            pass

        return False
