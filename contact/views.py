from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User as ZendeskUser

from django.conf import settings
from django.template.response import TemplateResponse
from django.views.generic.edit import FormView

from contact import forms


ZENPY_CREDENTIALS = {
    'email': settings.ZENDESK_EMAIL,
    'token': settings.ZENDESK_TOKEN,
    'subdomain': settings.ZENDESK_SUBDOMAIN
}
# Zenpy will let the connection timeout after 5s and will retry 3 times
zenpy_client = Zenpy(timeout=5, **ZENPY_CREDENTIALS)


class ReportIssueFormView(FormView):
    success_template = 'report_issue-success.html'
    template_name = 'report_issue.html'
    form_class = forms.ReportIssueForm

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(ReportIssueFormView, self).get_context_data(**kwargs)
        context['ENABLE_CAPTCHA'] = settings.ENABLE_CAPTCHA
        return context

    def get_or_create_zendesk_user(self, cleaned_data):
        zendesk_user = ZendeskUser(
            name=cleaned_data['name'],
            email=cleaned_data['email'],
        )
        return zenpy_client.users.create_or_update(zendesk_user)

    def create_zendesk_ticket(self, cleaned_data, zendesk_user):
        description = (
            'Name: {name}\n'
            'Email: {email}\n'
            'Feedback: {feedback}'
        ).format(**cleaned_data)
        ticket = Ticket(
            subject='Invest feedback',
            description=description,
            submitter_id=zendesk_user.id,
            requester_id=zendesk_user.id,
        )
        zenpy_client.tickets.create(ticket)

    def form_valid(self, form):
        if settings.ENABLE_CAPTCHA:
            zendesk_user = self.get_or_create_zendesk_user(form.cleaned_data)
            self.create_zendesk_ticket(form.cleaned_data, zendesk_user)
        return TemplateResponse(self.request, self.success_template)
