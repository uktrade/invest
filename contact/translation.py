from .models import ContactFormPage, FeedbackFormPage, ReportIssueFormPage, \
    ContactAgentEmail, ContactUserEmail, ContactFormSuccessPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(ContactFormPage)
class ContactFormPageTranslation(TranslationOptions):
    fields = (
        'heading',
    )


@register(ContactFormSuccessPage)
class ContactFormSuccessPageTranslation(TranslationOptions):
    fields = (
        'body_text',
    )


@register(FeedbackFormPage)
class FeedbackFormPageTranslation(TranslationOptions):
    fields = (
        'heading',
    )


@register(ReportIssueFormPage)
class ReportIssueFormPageTranslation(TranslationOptions):
    fields = (
        'heading',
    )


@register(ContactAgentEmail)
class ContactAgentEmailTranslation(TranslationOptions):
    fields = (
        'title',
        'heading',
        'body_text',
        'body_text_continued',
        'footer',
    )


@register(ContactUserEmail)
class ContactUserEmailTranslation(TranslationOptions):
    fields = (
        'title',
        'heading',
        'body_text',
        'body_text_continued',
        'footer',
    )
