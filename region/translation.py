from .models import RegionPage, RegionLandingPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(RegionPage)
class HomePageTranslation(TranslationOptions):
    fields = (
        'description',
        'heading',
        'subsections',
    )


@register(RegionLandingPage)
class HomePageTranslation(TranslationOptions):
    fields = (
        'heading',
    )
