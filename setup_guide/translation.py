from .models import SetupGuidePage, SetupGuideLandingPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(SetupGuidePage)
class HomePageTranslation(TranslationOptions):
    fields = (
        'description',
        'heading',
        'sub_heading',
        'subsections',
    )


@register(SetupGuideLandingPage)
class HomePageTranslation(TranslationOptions):
    fields = (
        'heading',
        'sub_heading',
    )
