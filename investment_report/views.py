import os
import datetime
import weasyprint

from itertools import product
from hashlib import md5
from collections import namedtuple


from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils import translation
from django.conf import settings

from investment_report.utils import (
    investment_report_generator, available_reports, get_investment_report_data
)

from investment_report.models import Market, Sector
from investment_report.forms import PIRForm

# Create your views here.
def investment_report(request, market, sector):
    market = get_object_or_404(Market, name=market)
    sector = get_object_or_404(Sector, name=sector)

    lang = request.GET.get('lang')
    if lang:
        translation.activate(lang)

    company = request.GET.get('company')

    return HttpResponse(
        str(investment_report_generator(market, sector, company, local=False))
    )


def investment_report_form(request):
    if request.method == "POST":
        form = PIRForm(request.POST)

        if form.is_valid():
            market = form.cleaned_data['market']
            sector = form.cleaned_data['sector']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']

            pdf_hash = '{}{}{}{}.pdf'.format(
                market.name, sector, company,
                datetime.date.today().isoformat()
            )

            request.session['report'] = {
                'email': email,
                'hash': pdf_hash
            }

            doc = weasyprint.HTML(
                string=investment_report_generator(market, sector, company)
            )

            doc.write_pdf(
                os.path.join(settings.MEDIA_ROOT, pdf_hash)
            )

            return redirect('pir_download')

        else:
            return render(request, 'pir_form.html', context={
                'form': form
            })

    return render(request, 'pir_form.html', context={
        'form': PIRForm()
    })


def investment_report_download(request):
    if 'report' not in request.session:
        return redirect('pir')

    path = os.path.join(settings.MEDIA_URL, request.session['report']['hash'])

    return render(request, 'pir_download.html', context={
        'download_link': path,
        'email': request.session['report']['email']
    })


def admin_table(request):
    template = loader.get_template('investment_report_table.html')

    markets = list(Market.objects.values_list('name', flat=True))
    sectors = list(Sector.objects.values_list('name', flat=True))
    languages = dict(settings.LANGUAGES).keys()

    reports = available_reports()

    return HttpResponse(template.render(context={
        'languages': languages,
        'markets': markets,
        'sectors': sectors,
        'reports': reports
    }))

def admin_table_detail(request, lang, market, sector):
    template = loader.get_template('investment_report_table_detail.html')
    translation.activate(lang)

    market = get_object_or_404(Market, name=market)
    sector = get_object_or_404(Sector, name=sector)
    ctx = get_investment_report_data(market, sector)

    translation.activate(settings.LANGUAGE_CODE)
    return HttpResponse(template.render(context={
        'pages': ctx,
    }))