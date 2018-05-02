import os
import pytest

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


@pytest.fixture()
def captcha_stub():
    # https://github.com/praekelt/django-recaptcha#id5
    os.environ['RECAPTCHA_TESTING'] = 'True'
    yield 'PASSED'
    os.environ['RECAPTCHA_TESTING'] = 'False'


@pytest.fixture()
def root_page():
    return Page.objects.filter(pk=1).get()


@pytest.fixture()
def home_page():
    return Page.objects.get(id=3)


@pytest.fixture()
def landing_page(home_page):
    landing = SectorLandingPage(**LANDING_DATA)
    home_page.add_child(instance=landing)
    return landing


@pytest.fixture()
def sector_pages(landing_page):
    sector1 = SectorPage(**SECTOR_DATA_1)
    sector2 = SectorPage(**SECTOR_DATA_2)

    landing_page.add_child(instance=sector1)
    landing_page.add_child(instance=sector2)

    return [sector1, sector2]
