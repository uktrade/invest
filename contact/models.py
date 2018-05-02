from gettext import gettext as _
from textwrap import dedent

from django.db.models import CharField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtailmarkdown.fields import MarkdownField

from wagtail.core.models import Page

from .views import ContactFormView, FeedbackFormView, ReportIssueFormView


class FormViewPage(Page):
    """
    Allow a wagtail Page to render a FormView.
    """
    def __init__(self, view, *args, **kwargs):
        self.view = view
        Page.__init__(self, *args, **kwargs)

    def serve(self, request):
        """
        Populate response with context from wagtail as well as
        FormView

        :param request:
        :return:
        """
        view = self.view.as_view()

        response = view(request)

        # NOTE: response.context_data == None when the form is submitted
        # it may need to be handled differently than this:
        if response.context_data is None:
            response.context_data = {}

        response.context_data['page'] = self
        response.context_data['self'] = self

        return response


class ContactFormPage(FormViewPage):
    def __init__(self, *args, **kwargs):
        FormViewPage.__init__(self, ContactFormView, *args, **kwargs)

    heading = CharField(max_length=255, default=_("Contact Us"))

    content_panels = Page.content_panels + [
        FieldPanel('heading')
    ]


class FeedbackFormPage(FormViewPage):
    def __init__(self, *args, **kwargs):
        FormViewPage.__init__(self, FeedbackFormView, *args, **kwargs)

    heading = CharField(max_length=255, default=_("Feedback"))

    content_panels = Page.content_panels + [
        FieldPanel('heading')
    ]


class ReportIssueFormPage(FormViewPage):
    def __init__(self, *args, **kwargs):
        FormViewPage.__init__(self, ReportIssueFormView, *args, **kwargs)

    view = ReportIssueFormView
    heading = CharField(max_length=255, default=_("Report Issue"))

    content_panels = Page.content_panels + [
        FieldPanel('heading')
    ]


class ContactFormSuccessPage(Page):
    body_text = MarkdownField()

    content_panels = [
        FieldPanel('title'),
        FieldPanel('body_text'),
    ]


@register_setting
class ContactUserEmail(BaseSetting):

    title = CharField(
        max_length=255,
        default="Invest in GREAT Britain",
    )

    heading = CharField(
        max_length=255,
        default="Invest in GREAT Britain Contact Confirmation"
    )

    body_text = MarkdownField(
        default=dedent("""
            Thank you for contacting the Department for International Trade about your investment plans.
            
            We have received the information you sent through the Invest in Great Britain website and will aim to follow up with
            you in the next 7 days. Your enquiry may be forwarded to a local post for follow up.
            
            The Department for International Trade provides free and impartial advice to companies around the world interested in
            doing business in the UK. We look forward to welcoming you as one of the many companies to enjoy success in the UK.
            Find our Terms and Conditions [here](http://https://invest.great.gov.uk/int/terms-and-conditions/).
            
            See below for your submitted form:"""))  # noqa

    body_text_continued = MarkdownField(
        default=dedent("""
            Many Thanks
            
            DIT"""    # noqa
    ))

    footer = MarkdownField(
        default=dedent("""
            Department for International Trade (DIT) is the Government Department that helps UK‑based companies succeed in the
            global economy. We also help overseas companies bring their high-quality investment to the UK’s dynamic economy,
            acknowledged as Europe’s best place in which to succeed in global business.
            
            [invest.great.gov.uk](http://https://invest.great.gov.uk)"""))  # noqa

    panels = [
        FieldPanel('title'),
        FieldPanel('heading'),
        FieldPanel('body_text'),
        FieldPanel('body_text_continued'),
        FieldPanel('footer'),
    ]


@register_setting
class ContactAgentEmail(BaseSetting):

    title = CharField(
        max_length=255,
        default="Invest in GREAT Britain",
    )

    heading = CharField(
        max_length=255,
        default="Invest in GREAT Britain Contact Confirmation"
    )

    body_text = MarkdownField(
        default=dedent("""
            This is confirmation of an Invest in Great Britain lead via the contact us form on the website.
            
            See below for the user submitted form:""")  # noqa
    )

    body_text_continued = MarkdownField(
        default=dedent("""
            Many Thanks
            
            DIT""")  # noqa
    )

    footer = MarkdownField(
        default=dedent("""
            Department for International Trade (DIT) is the Government Department that helps UK‑based companies succeed in the
            global economy. We also help overseas companies bring their high-quality investment to the UK’s dynamic economy,
            acknowledged as Europe’s best place in which to succeed in global business.
            
            [invest.great.gov.uk](http://https://invest.great.gov.uk)""")   # noqa
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('heading'),
        FieldPanel('body_text'),
        FieldPanel('body_text_continued'),
        FieldPanel('footer'),
    ]
