from .models import ContactFormPage, FeedbackFormPage, ReportIssueFormPage, ContactAgentEmail, ContactUserEmail
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(ContactFormPage)
class ContactFormPageTranslation(TranslationOptions):
    fields = (
        'heading',
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
