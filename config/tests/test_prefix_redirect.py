import pytest
from django.http import Http404

from django.test import RequestFactory
from wagtail.core.models import Site

from config import redirect
from config.redirect_mt import MTRedirectPrefixedPage


def setup_class_based_view(view, request, *args, **kwargs):
    """Mimic ``as_view()``, but returns view instance.
    Use this function to get view instances on which you can run unit tests,
    by testing specific methods."""
    # noqa from https://stackoverflow.com/questions/33645780/how-to-unit-test-methods-inside-djangos-class-based-views
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view()


def class_based_view_instance(view, request, *args, **kwargs):
    view = setup_class_based_view(view, request, *args, **kwargs)
    return view()


def request_path(path):
    factory = RequestFactory()
    request = factory.get(path)
    request.site = Site.find_for_request(request)
    return request


def call_get_redirect_url(klass, path, debug=False):
    """
    Call get_redirect_url with a test request on CBV.

    :param klass: RedirectView derived class
    :param path: path to call redirect
    :return: result of get_redirect_url, request
    """
    request = request_path(path)
    view = setup_class_based_view(klass, request)
    result = view.get_redirect_url()
    return result, request


@pytest.mark.django_db
def test_needs_prefix_map():
    class TestRedirect(MTRedirectPrefixedPage):
        # no prefix_map attribute,
        pass

    with pytest.raises(AttributeError):
        TestRedirect()


@pytest.mark.django_db
def test_prefix_as_urls():
    class TestRedirect(MTRedirectPrefixedPage):
        prefix_map = [('int/a', 'a'), ('int', '/')]
        pass

    assert TestRedirect.as_urls() == 'int/a|int'


@pytest.mark.django_db
@pytest.mark.parametrize(
    'path, expected',
    (
        ('/planets/pluto/charon/', '/dwarf-planets/pluto/charon/'),
        ('/planets/pluto/', '/dwarf-planets/pluto/'),
        ('/planets/venus/', '/planets/venus/'),
        ('/asteroids/vesta/', '/asteroids/vesta/'),
    ),
)
def test_prefix_mappings(path, expected):
    class ExampleRedirector(redirect.RedirectPrefixes):
        prefix_map = [('planets/pluto/', 'dwarf-planets/pluto/')]

    result, request = call_get_redirect_url(ExampleRedirector, path)
    assert request.path == expected


@pytest.mark.django_db
def test_prefix_page_redirect(client, root_page, landing_page, sector_pages):
    response = client.get('/industries/')
    request = response.wsgi_request

    path_components = '/industries'.split('/')
    route = root_page.specific.route(request, path_components)
    assert route.page == landing_page

    class LangRedirect(MTRedirectPrefixedPage):
        prefix_map = [('en/', '/')]

    _, request = call_get_redirect_url(LangRedirect, '/')
    assert(request.path == '/')

    _, request = call_get_redirect_url(LangRedirect, '/en/')
    assert(request.path == '/')

    _, request = call_get_redirect_url(
        LangRedirect, '/en/industries/aerospace/')
    assert (request.path == '/industries/aerospace/')

    with pytest.raises(Http404):
        _, request = call_get_redirect_url(
            LangRedirect, '/en/industries/non-existant/')
