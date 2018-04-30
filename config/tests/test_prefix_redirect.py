import pytest
from django.http import Http404

from django.test import RequestFactory
from wagtail.core.models import Site

from config import redirect
from config.redirect_mt import MTRedirectPrefixedPage

from wagtail.core.models import Page
from sector.models import SectorPage, SectorLandingPage


def build_page_data(name, **kwargs):
    return dict(
        title_en=name,
        slug_en=name,
        heading_en="test_%s heading" % name,
        **kwargs
    )


def build_sector_data(name):
    return build_page_data(name, description_en='test_%s description')


LANDING_DATA = build_page_data('industries')
SECTOR_DATA_1 = build_sector_data('aerospace')
SECTOR_DATA_2 = build_sector_data('creative')


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


@pytest.fixture(scope="session")
def root_page():
    return Page.objects.filter(pk=1).get()


@pytest.fixture(scope="session")
def home_page():
    return Page.objects.get(id=3)


@pytest.fixture(scope="session")
def landing_page(home_page):
    landing = SectorLandingPage(**LANDING_DATA)
    home_page.add_child(instance=landing)
    return landing


@pytest.fixture(scope="session")
def sector_pages(landing_page):
    sector1 = SectorPage(**SECTOR_DATA_1)
    sector2 = SectorPage(**SECTOR_DATA_2)

    landing_page.add_child(instance=sector1)
    landing_page.add_child(instance=sector2)

    return [sector1, sector2]


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
