from .models import RegionPage, RegionLandingPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(RegionPage)
class RegionPageTranslation(TranslationOptions):
    fields = (
        'description',
        'heading',
        'subsections',
    )


@register(RegionLandingPage)
class RegionLandingPageTranslation(TranslationOptions):
    fields = (
        'heading',
    )
