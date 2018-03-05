from .models import HomePage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(HomePage)
class HomePageTranslation(TranslationOptions):
    fields = (
        'heading',
        'sub_heading',
        'how_we_help',
    )
