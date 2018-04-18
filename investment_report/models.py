from bs4 import BeautifulSoup
from collections import OrderedDict

from sorl.thumbnail import ImageField

from django.db import models
from django.utils.html import format_html

from markdownx.models import MarkdownxField


class Sector(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MarketLogo(models.Model):
    name = models.CharField(max_length=255)
    image = ImageField()

    def __str__(self):
        return self.name


class SectorLogo(models.Model):
    name = models.CharField(max_length=255)
    image = ImageField()

    def __str__(self):
        return self.name


class PDFSection(models.Model):
    SINGLETON = False
    SECTION = 999
    TRANSLATION_FIELDS = ['content']

    content = MarkdownxField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.content[:10]


# Begin spam of table models.
class FrontPage(PDFSection):
    SECTION = 0
    SINGLETON = True
    TRANSLATION_FIELDS = []

    def __str__(self):
        return '4 - UK Market Overview'

    # No body
    content = None
    background_image = models.FileField()

    class Meta:
        verbose_name = verbose_name_plural = '0 - Front Page'


class SectorOverview(PDFSection):
    SECTION = 1
    TRANSLATION_FIELDS = (
        PDFSection.TRANSLATION_FIELDS + 
        ['footer_image_copy', 'footer_image_copy_attribution']
    )

    sector = models.ForeignKey(Sector, unique=True)
    footer_image = models.ImageField()
    footer_image_copy = models.TextField(blank=True)
    footer_image_copy_attribution = models.TextField(blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '1 - Sector Overview'


class KillerFacts(PDFSection):
    SECTION = 2
    sector = models.ForeignKey(Sector, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = '2 - Killer Facts'


class MacroContextBetweenCountries(PDFSection):
    SECTION = 3
    market = models.ForeignKey(Market, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = '3 - Macro Context'


class UKMarketOverview(PDFSection):
    SECTION = 4
    SINGLETON = True
    TRANSLATION_FIELDS = []

    def __str__(self):
        return '4 - UK Market Overview'

    # No body
    content = None
    body_image = models.FileField()
    background_image = models.ImageField()

    class Meta:
        verbose_name = verbose_name_plural = '4 - UK Market Overview'


class UKBusinessInfo(PDFSection):
    SECTION = 5
    SINGLETON = True
    TRANSLATION_FIELDS = []

    def __str__(self):
        return '5 - Business Info'

    # No body
    content = None
    body_image = models.FileField()
    background_image = models.ImageField()

    class Meta:
        verbose_name = verbose_name_plural = '5 - Business Info'


class UKGeographicOverview(PDFSection):
    SECTION = 6
    SINGLETON = True

    class Meta:
        verbose_name = verbose_name_plural = '6 - Geographic Overview'


class TalentAndEducationGeneric(PDFSection):
    SECTION = 7.1
    SINGLETON = True

    class Meta:
        verbose_name = verbose_name_plural = '7.1 - Talent & Education (Generic)'


class TalentAndEducationBySector(PDFSection):
    SECTION = 7.2
    sector = models.ForeignKey(Sector, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = '7.2 - Talent & Education (Sector)'


class SectorInitiatives(PDFSection):
    SECTION = 8
    sector = models.ForeignKey(Sector, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = '8 - Sector Initiatives'


class NetworkAndSupport(PDFSection):
    SECTION = 9
    background_image = models.ImageField()

    class Meta:
        verbose_name = verbose_name_plural = '9 - Network And Support'


class RDandInnovation(PDFSection):
    SECTION = 10
    sector = models.ForeignKey(Sector, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = '10 - R&D and Innovation'


class RDandInnovationCaseStudy(PDFSection):
    SECTION = 11
    sector = models.ForeignKey(Sector, unique=True)

    class Meta:
        verbose_name = verbose_name_plural = '11 - Case Study'


class WhoIsHere(PDFSection):
    SECTION = 12
    TRANSLATION_FIELDS = []
    background_image = models.ImageField()

    def __str__(self):
        return '12 - Who\'s here background'

    # No body
    content = None

    class Meta:
        verbose_name = verbose_name_plural = '12 - Who\'s here (background image)'


class VideoCaseStudy(PDFSection):
    """
    Todo:
    """
    SECTION = 13
    sector = models.ForeignKey(Sector, unique=True)


class ServicesOfferedByDIT(PDFSection):
    SECTION = 14
    SINGLETON = True
    footer_image = models.ImageField()

    class Meta:
        verbose_name = verbose_name_plural = '14 - Services Offered'


class CallToAction(PDFSection):
    SECTION = 15
    SINGLETON = True

    class Meta:
        verbose_name = verbose_name_plural = '15 - Call to action'



class Contact(PDFSection):
    SECTION = 17
    SINGLETON = True

    TRANSLATION_FIELDS = (
        PDFSection.TRANSLATION_FIELDS + 
        ['title', ]
    )

    title = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    background_image = models.ImageField()

    class Meta:
        verbose_name = verbose_name_plural = '17 - Contact'


class Testimonials(PDFSection):
    SECTION = 16
    SINGLETON = True

    class Meta:
        verbose_name = verbose_name_plural = '16 - Testimonials'


sections = sorted(PDFSection.__subclasses__(), key=lambda x: x.SECTION)

page_registry = OrderedDict({
    m.__name__: m for m in sections
})