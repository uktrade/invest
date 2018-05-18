from django.conf.urls import url
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views import View
from django.views.generic import RedirectView


class NotFoundView(View):
    def dispatch(self, request, *args, **kwargs):
        return HttpResponseNotFound()


class ServerErrorView(View):
    def dispatch(self, request, *args, **kwargs):
        return HttpResponseServerError()


urlpatterns = [
    #  ($|index\.html$) either end of string $ or index.html

    # /int/ar/ -> /ar/
    url(
        r'^int/ar/($|index\.html$)',
        RedirectView.as_view(url='/ar/', permanent=True),
    ),
    url(
        r'^int/ar/404.html',
        NotFoundView.as_view(),
    ),
    url(
        r'^int/ar/500.html',
        ServerErrorView.as_view,
    ),
    url(
        r'^int/ar/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/ar/setup-guide/', permanent=True),
    ),
    url(
        r'^int/ar/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/ar/setup-guide/establish-address/',
                             permanent=True),
    ),
    url(
        r'^int/ar/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/ar/setup-guide/apply-for-visa/',
                             permanent=True),
    ),
    url(
        r'^int/ar/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/ar/setup-guide/open-a-business-account/',
                             permanent=True),
    ),
    url(
        r'^int/ar/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/ar/setup-guide/how-to-setup/',
                             permanent=True),
    ),
    url(
        r'^int/ar/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/ar/setup-guide/understand-tax/',
                             permanent=True),
    ),
    url(
        r'^int/ar/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/ar/setup-guide/access-talent/',
                             permanent=True),
    ),
    url(
        r'^int/ar/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/ar/setup-guide/understand-legal/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/', permanent=True),
    ),
    url(
        r'^int/ar/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/aerospace/', permanent=True),
    ),
    url(
        r'^int/ar/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/advanced-manufacturing/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(
            url='/ar/industries/food-and-drink-manufacturing/',
            permanent=True),
    ),
    url(
        r'^int/ar/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ar/industries/food-and-drink-manufacturing/freefrom/',
            permanent=True),
    ),
    url(
        r'^int/ar/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/retail/', permanent=True),
    ),
    url(
        r'^int/ar/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/automotive/', permanent=True),
    ),
    url(
        r'^int/ar/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/automotive/motorsport/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/automotive/research-and-development/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ar/industries/automotive/research-and-development/',
            permanent=True),
    ),
    url(
        r'^int/ar/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/automotive/supply-chain/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/energy/', permanent=True),
    ),
    url(
        r'^int/ar/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/energy/offshore-wind/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/energy/electrical-networks/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/energy/energy-from-waste/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/energy/oil-and-gas/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/energy/nuclear/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/health-and-life/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/health-and-life/medical-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ar/industries/health-and-life/medical-technology/',
            permanent=True),
    ),
    url(
        r'^int/ar/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ar/industries/health-and-life/pharmaceutical-manufacturing/',
            permanent=True),
    ),
    url(
        r'^int/ar/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/creative/', permanent=True),
    ),
    url(
        r'^int/ar/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/ar/industries/creative/content-and-production/',
            permanent=True),
    ),
    url(
        r'^int/ar/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/creative/digital-media/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/financial-services/',
                             permanent=True),
    ),
    url(
        r'^int/ar/industries/financial-services/asset-management/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ar/industries/financial-services/asset-management/',
            permanent=True),
    ),
    url(
        r'^int/ar/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ar/industries/financial-services/financial-technology/',
            permanent=True),
    ),
    url(
        r'^int/ar/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/technology/', permanent=True),
    ),
    url(
        r'^int/ar/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/ar/industries/technology/data-analytics/',
                             permanent=True),
    ),
    url(
        r'^int/ar/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/ar/terms-and-conditions/', permanent=True),
    ),
    url(
        r'^int/ar/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/ar/privacy-policy/', permanent=True),
    ),
    url(
        r'^int/ar/feedback/($|index\.html$)',
        RedirectView.as_view(url='/ar/feedback/', permanent=True),
    ),
    url(
        r'^int/ar/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/ar/enquiries/confirmation/',
                             permanent=True),
    ),
    url(
        r'^int/ar/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/ar/enquiries/error/', permanent=True),
    ),
    url(
        r'^int/ar/contact/($|index\.html$)',
        RedirectView.as_view(url='/ar/contact/', permanent=True),
    ),
    url(
        r'^int/ar/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/ar/location-guide/', permanent=True),
    ),
    url(
        r'^int/ar/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/ar/location-guide/confirmation/',
                             permanent=True),
    ),

    # /int/de
    url(
        r'^int/de/($|index\.html$)',
        RedirectView.as_view(url='/de', permanent=True),
    ),
    url(
        r'^int/de/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^int/de/500.html$',
        ServerErrorView.as_view()
    ),
    url(
        r'^int/de/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/de/setup-guide', permanent=True),
    ),
    url(
        r'^int/de/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/de/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^int/de/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/de/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^int/de/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/de/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^int/de/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/de/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^int/de/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/de/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^int/de/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/de/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^int/de/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/de/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/($|index\.html$)',
        RedirectView.as_view(url='/de/industries', permanent=True),
    ),
    url(
        r'^int/de/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/aerospace', permanent=True),
    ),
    url(
        r'^int/de/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/de/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^int/de/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/retail', permanent=True),
    ),
    url(
        r'^int/de/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/automotive', permanent=True),
    ),
    url(
        r'^int/de/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/automotive/research-and-development/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/de/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^int/de/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/energy', permanent=True),
    ),
    url(
        r'^int/de/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/health-and-life/medical-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/de/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^int/de/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/de/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^int/de/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/creative', permanent=True),
    ),
    url(
        r'^int/de/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/de/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^int/de/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^int/de/industries/financial-services/asset-management/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/de/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^int/de/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/de/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^int/de/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/technology', permanent=True),
    ),
    url(
        r'^int/de/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/de/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^int/de/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/de/terms-and-conditions', permanent=True),
    ),
    url(
        r'^int/de/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/de/privacy-policy', permanent=True),
    ),
    url(
        r'^int/de/feedback/($|index\.html$)',
        RedirectView.as_view(url='/de/feedback', permanent=True),
    ),
    url(
        r'^int/de/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/de/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^int/de/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/de/enquiries/error', permanent=True),
    ),
    url(
        r'^int/de/contact/($|index\.html$)',
        RedirectView.as_view(url='/de/contact', permanent=True),
    ),
    url(
        r'^int/de/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/de/location-guide', permanent=True),
    ),
    url(
        r'^int/de/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/de/location-guide/confirmation',
                             permanent=True),
    ),

    #  int/es
    url(
        r'^int/es/($|index\.html$)',
        RedirectView.as_view(url='/es', permanent=True),
    ),
    url(
        r'^int/es/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^int/es/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^int/es/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/es/setup-guide', permanent=True),
    ),
    url(
        r'^int/es/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/es/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^int/es/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/es/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^int/es/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/es/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^int/es/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/es/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^int/es/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/es/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^int/es/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/es/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^int/es/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/es/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/($|index\.html$)',
        RedirectView.as_view(url='/es/industries', permanent=True),
    ),
    url(
        r'^int/es/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/aerospace', permanent=True),
    ),
    url(
        r'^int/es/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/es/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^int/es/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/retail', permanent=True),
    ),
    url(
        r'^int/es/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/automotive', permanent=True),
    ),
    url(
        r'^int/es/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/automotive/research-and-development/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/es/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^int/es/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/energy', permanent=True),
    ),
    url(
        r'^int/es/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/health-and-life/medical-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/es/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^int/es/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/es/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^int/es/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/creative', permanent=True),
    ),
    url(
        r'^int/es/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/es/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^int/es/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^int/es/industries/financial-services/asset-management/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/es/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^int/es/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/es/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^int/es/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/technology', permanent=True),
    ),
    url(
        r'^int/es/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/es/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^int/es/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/es/terms-and-conditions', permanent=True),
    ),
    url(
        r'^int/es/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/es/privacy-policy', permanent=True),
    ),
    url(
        r'^int/es/feedback/($|index\.html$)',
        RedirectView.as_view(url='/es/feedback', permanent=True),
    ),
    url(
        r'^int/es/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/es/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^int/es/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/es/enquiries/error', permanent=True),
    ),
    url(
        r'^int/es/contact/($|index\.html$)',
        RedirectView.as_view(url='/es/contact', permanent=True),
    ),
    url(
        r'^int/es/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/es/location-guide', permanent=True),
    ),
    url(
        r'^int/es/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/es/location-guide/confirmation',
                             permanent=True),
    ),

    # /int/fr/
    url(
        r'^int/fr/($|index\.html$)',
        RedirectView.as_view(url='/fr', permanent=True),
    ),
    url(
        r'^int/fr/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^int/fr/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^int/fr/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/fr/setup-guide', permanent=True),
    ),
    url(
        r'^int/fr/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/fr/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^int/fr/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/fr/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^int/fr/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/fr/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^int/fr/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/fr/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^int/fr/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/fr/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^int/fr/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/fr/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^int/fr/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/fr/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries', permanent=True),
    ),
    url(
        r'^int/fr/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/aerospace', permanent=True),
    ),
    url(
        r'^int/fr/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/fr/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^int/fr/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/retail', permanent=True),
    ),
    url(
        r'^int/fr/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/automotive', permanent=True),
    ),
    url(
        r'^int/fr/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/automotive/research-and-development/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/fr/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^int/fr/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/energy', permanent=True),
    ),
    url(
        r'^int/fr/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/health-and-life/medical-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/fr/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^int/fr/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/fr/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^int/fr/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/creative', permanent=True),
    ),
    url(
        r'^int/fr/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/fr/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^int/fr/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^int/fr/industries/financial-services/asset-management/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/fr/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^int/fr/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/fr/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^int/fr/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/technology', permanent=True),
    ),
    url(
        r'^int/fr/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/fr/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^int/fr/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/fr/terms-and-conditions', permanent=True),
    ),
    url(
        r'^int/fr/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/fr/privacy-policy', permanent=True),
    ),
    url(
        r'^int/fr/feedback/($|index\.html$)',
        RedirectView.as_view(url='/fr/feedback', permanent=True),
    ),
    url(
        r'^int/fr/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/fr/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^int/fr/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/fr/enquiries/error', permanent=True),
    ),
    url(
        r'^int/fr/contact/($|index\.html$)',
        RedirectView.as_view(url='/fr/contact', permanent=True),
    ),
    url(
        r'^int/fr/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/fr/location-guide', permanent=True),
    ),
    url(
        r'^int/fr/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/fr/location-guide/confirmation',
                             permanent=True),
    ),

    # /int/ja
    url(
        r'^int/ja/($|index\.html$)',
        RedirectView.as_view(url='/ja', permanent=True),
    ),
    url(
        r'^int/ja/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^int/ja/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^int/ja/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide', permanent=True),
    ),
    url(
        r'^int/ja/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^int/ja/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^int/ja/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^int/ja/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^int/ja/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^int/ja/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^int/ja/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries', permanent=True),
    ),
    url(
        r'^int/ja/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/aerospace', permanent=True),
    ),
    url(
        r'^int/ja/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ja/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^int/ja/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/retail', permanent=True),
    ),
    url(
        r'^int/ja/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/automotive', permanent=True),
    ),
    url(
        r'^int/ja/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/automotive/research-and-development/($|index\.html$)',  # noqa
         RedirectView.as_view(
            url='/ja/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^int/ja/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy', permanent=True),
    ),
    url(
        r'^int/ja/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/health-and-life/medical-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ja/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^int/ja/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ja/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^int/ja/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/creative', permanent=True),
    ),
    url(
        r'^int/ja/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/ja/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^int/ja/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^int/ja/industries/financial-services/asset-management/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ja/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^int/ja/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ja/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^int/ja/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/technology', permanent=True),
    ),
    url(
        r'^int/ja/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^int/ja/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/ja/terms-and-conditions', permanent=True),
    ),
    url(
        r'^int/ja/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/ja/privacy-policy', permanent=True),
    ),
    url(
        r'^int/ja/feedback/($|index\.html$)',
        RedirectView.as_view(url='/ja/feedback', permanent=True),
    ),
    url(
        r'^int/ja/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/ja/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^int/ja/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/ja/enquiries/error', permanent=True),
    ),
    url(
        r'^int/ja/contact/($|index\.html$)',
        RedirectView.as_view(url='/ja/contact', permanent=True),
    ),
    url(
        r'^int/ja/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/ja/location-guide', permanent=True),
    ),
    url(
        r'^int/ja/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/ja/location-guide/confirmation',
                             permanent=True),
    ),


    # /int/pt
    url(
        r'^int/pt/($|index\.html$)',
        RedirectView.as_view(url='/pt', permanent=True),
    ),
    url(
        r'^int/pt/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^int/pt/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^int/pt/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide', permanent=True),
    ),
    url(
        r'^int/pt/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^int/pt/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^int/pt/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^int/pt/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^int/pt/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^int/pt/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^int/pt/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries', permanent=True),
    ),
    url(
        r'^int/pt/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/aerospace', permanent=True),
    ),
    url(
        r'^int/pt/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^int/pt/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/retail', permanent=True),
    ),
    url(
        r'^int/pt/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/automotive', permanent=True),
    ),
    url(
        r'^int/pt/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/automotive/research-and-development/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^int/pt/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy', permanent=True),
    ),
    url(
        r'^int/pt/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/health-and-life/medical-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^int/pt/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^int/pt/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/creative', permanent=True),
    ),
    url(
        r'^int/pt/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/pt/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^int/pt/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^int/pt/industries/financial-services/asset-management/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^int/pt/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^int/pt/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/technology', permanent=True),
    ),
    url(
        r'^int/pt/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^int/pt/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/pt/terms-and-conditions', permanent=True),
    ),
    url(
        r'^int/pt/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/pt/privacy-policy', permanent=True),
    ),
    url(
        r'^int/pt/feedback/($|index\.html$)',
        RedirectView.as_view(url='/pt/feedback', permanent=True),
    ),
    url(
        r'^int/pt/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/pt/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^int/pt/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/pt/enquiries/error', permanent=True),
    ),
    url(
        r'^int/pt/contact/($|index\.html$)',
        RedirectView.as_view(url='/pt/contact', permanent=True),
    ),
    url(
        r'^int/pt/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/pt/location-guide', permanent=True),
    ),
    url(
        r'^int/pt/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/pt/location-guide/confirmation',
                             permanent=True),
    ),

    # int/zh
    url(
        r'^int/zh/($|index\.html$)',
        RedirectView.as_view(url='/zh', permanent=True),
    ),
    url(
        r'^int/zh/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^int/zh/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^int/zh/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/zh/setup-guide', permanent=True),
    ),
    url(
        r'^int/zh/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/zh/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^int/zh/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/zh/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^int/zh/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/zh/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^int/zh/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/zh/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^int/zh/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/zh/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^int/zh/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/zh/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^int/zh/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/zh/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries', permanent=True),
    ),
    url(
        r'^int/zh/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/aerospace', permanent=True),
    ),
    url(
        r'^int/zh/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',
        RedirectView.as_view(
            url='/zh/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^int/zh/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/retail', permanent=True),
    ),
    url(
        r'^int/zh/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/automotive', permanent=True),
    ),
    url(
        r'^int/zh/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/automotive/research-and-development/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/zh/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^int/zh/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/energy', permanent=True),
    ),
    url(
        r'^int/zh/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/health-and-life/medical-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/zh/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^int/zh/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/zh/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^int/zh/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/creative', permanent=True),
    ),
    url(
        r'^int/zh/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/zh/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^int/zh/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^int/zh/industries/financial-services/asset-management/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/zh/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^int/zh/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/zh/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^int/zh/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/technology', permanent=True),
    ),
    url(
        r'^int/zh/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/zh/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^int/zh/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/zh/terms-and-conditions', permanent=True),
    ),
    url(
        r'^int/zh/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/zh/privacy-policy', permanent=True),
    ),
    url(
        r'^int/zh/feedback/($|index\.html$)',
        RedirectView.as_view(url='/zh/feedback', permanent=True),
    ),
    url(
        r'^int/zh/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/zh/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^int/zh/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/zh/enquiries/error', permanent=True),
    ),
    url(
        r'^int/zh/contact/($|index\.html$)',
        RedirectView.as_view(url='/zh/contact', permanent=True),
    ),
    url(
        r'^int/zh/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/zh/location-guide', permanent=True),
    ),
    url(
        r'^int/zh/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/zh/location-guide/confirmation',
                             permanent=True),
    ),


    # cn
    url(
        r'^cn/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn', permanent=True),
    ),
    url(
        r'^cn/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^cn/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^cn/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/setup-guide', permanent=True),
    ),
    url(
        r'^cn/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^cn/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^cn/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^cn/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^cn/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^cn/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^cn/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^cn/industries/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries', permanent=True),
    ),
    url(
        r'^cn/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/aerospace', permanent=True),
    ),
    url(
        r'^cn/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^cn/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(
            url='/zh-cn/industries/food-and-drink-manufacturing',
            permanent=True),
    ),
    url(
        r'^cn/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/zh-cn/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^cn/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/retail', permanent=True),
    ),
    url(
        r'^cn/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/automotive',
                             permanent=True),
    ),
    url(
        r'^cn/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^cn/industries/automotive/research-and-development/($|index\.html$)',
        RedirectView.as_view(
            url='/zh-cn/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^cn/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^cn/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/energy', permanent=True),
    ),
    url(
        r'^cn/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^cn/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^cn/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^cn/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^cn/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^cn/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^cn/industries/health-and-life/medical-technology/($|index\.html$)',
        RedirectView.as_view(
            url='/zh-cn/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^cn/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/zh-cn/industries/health-and-life/pharmaceutical-manufacturing',  # noqa
            permanent=True),
    ),
    url(
        r'^cn/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/creative', permanent=True),
    ),
    url(
        r'^cn/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/zh-cn/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^cn/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^cn/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^cn/industries/financial-services/asset-management/($|index\.html$)',
        RedirectView.as_view(
            url='/zh-cn/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^cn/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/zh-cn/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^cn/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/technology',
                             permanent=True),
    ),
    url(
        r'^cn/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^cn/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/terms-and-conditions', permanent=True),
    ),
    url(
        r'^cn/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/privacy-policy', permanent=True),
    ),
    url(
        r'^cn/feedback/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/feedback', permanent=True),
    ),
    url(
        r'^cn/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/enquiries/confirmation',
                             permanent=True),
    ),
    url(
        r'^cn/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/enquiries/error', permanent=True),
    ),
    url(
        r'^cn/contact/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/contact', permanent=True),
    ),
    url(
        r'^cn/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/location-guide', permanent=True),
    ),
    url(
        r'^cn/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/zh-cn/location-guide/confirmation',
                             permanent=True),
    ),

    # br/
    url(
        r'^br/($|index\.html$)',
        RedirectView.as_view(url='/pt/', permanent=True),
    ),
    url(
        r'^br/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^br/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^br/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide', permanent=True),
    ),
    url(
        r'^br/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^br/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^br/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^br/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^br/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^br/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^br/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/pt/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^br/industries/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries', permanent=True),
    ),
    url(
        r'^br/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/aerospace', permanent=True),
    ),
    url(
        r'^br/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^br/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^br/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^br/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/retail', permanent=True),
    ),
    url(
        r'^br/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/automotive', permanent=True),
    ),
    url(
        r'^br/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^br/industries/automotive/research-and-development/($|index\.html$)',
        RedirectView.as_view(
            url='/pt/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^br/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^br/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy', permanent=True),
    ),
    url(
        r'^br/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^br/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^br/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^br/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^br/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^br/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^br/industries/health-and-life/medical-technology/($|index\.html$)',
        RedirectView.as_view(
            url='/pt/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^br/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^br/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/creative', permanent=True),
    ),
    url(
        r'^br/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/pt/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^br/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^br/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^br/industries/financial-services/asset-management/($|index\.html$)',
        RedirectView.as_view(
            url='/pt/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^br/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/pt/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^br/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/technology', permanent=True),
    ),
    url(
        r'^br/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/pt/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^br/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/pt/terms-and-conditions', permanent=True),
    ),
    url(
        r'^br/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/pt/privacy-policy', permanent=True),
    ),
    url(
        r'^br/feedback/($|index\.html$)',
        RedirectView.as_view(url='/pt/feedback', permanent=True),
    ),
    url(
        r'^br/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/pt/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^br/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/pt/enquiries/error', permanent=True),
    ),
    url(
        r'^br/contact/($|index\.html$)',
        RedirectView.as_view(url='/pt/contact', permanent=True),
    ),
    url(
        r'^br/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/pt/location-guide', permanent=True),
    ),
    url(
        r'^br/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/pt/location-guide/confirmation',
                             permanent=True),
    ),


    # jp/ -> ja/
    url(
        r'^jp/($|index\.html$)',
        RedirectView.as_view(url='/ja/', permanent=True),
    ),
    url(
        r'^jp/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^jp/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^jp/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide', permanent=True),
    ),
    url(
        r'^jp/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^jp/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^jp/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^jp/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/how-to-setup',
                             permanent=True),
    ),
    url(
        r'^jp/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^jp/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/access-talent',
                             permanent=True),
    ),
    url(
        r'^jp/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/ja/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^jp/industries/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries', permanent=True),
    ),
    url(
        r'^jp/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/aerospace', permanent=True),
    ),
    url(
        r'^jp/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^jp/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^jp/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ja/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^jp/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/retail', permanent=True),
    ),
    url(
        r'^jp/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/automotive', permanent=True),
    ),
    url(
        r'^jp/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^jp/industries/automotive/research-and-development/($|index\.html$)',
        RedirectView.as_view(
            url='/ja/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^jp/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^jp/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy', permanent=True),
    ),
    url(
        r'^jp/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^jp/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^jp/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^jp/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^jp/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/energy/nuclear',
                             permanent=True),
    ),
    url(
        r'^jp/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^jp/industries/health-and-life/medical-technology/($|index\.html$)',
        RedirectView.as_view(
            url='/ja/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^jp/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ja/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^jp/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/creative', permanent=True),
    ),
    url(
        r'^jp/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(
            url='/ja/industries/creative/content-and-production',
            permanent=True),
    ),
    url(
        r'^jp/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^jp/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^jp/industries/financial-services/asset-management/($|index\.html$)',
        RedirectView.as_view(
            url='/ja/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^jp/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/ja/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^jp/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/technology', permanent=True),
    ),
    url(
        r'^jp/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/ja/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^jp/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/ja/terms-and-conditions', permanent=True),
    ),
    url(
        r'^jp/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/ja/privacy-policy', permanent=True),
    ),
    url(
        r'^jp/feedback/($|index\.html$)',
        RedirectView.as_view(url='/ja/feedback', permanent=True),
    ),
    url(
        r'^jp/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/ja/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^jp/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/ja/enquiries/error', permanent=True),
    ),
    url(
        r'^jp/contact/($|index\.html$)',
        RedirectView.as_view(url='/ja/contact', permanent=True),
    ),
    url(
        r'^jp/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/ja/location-guide', permanent=True),
    ),
    url(
        r'^jp/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/ja/location-guide/confirmation',
                             permanent=True),
    ),

    # /in/ -> /
    url(
        r'^in/($|index\.html$)',
        RedirectView.as_view(url='/', permanent=True),
    ),
    url(
        r'^in/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^in/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^in/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide', permanent=True),
    ),
    url(
        r'^in/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^in/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/apply-for-visa', permanent=True),  # noqa
    ),
    url(
        r'^in/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^in/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/how-to-setup', permanent=True),
    ),
    url(
        r'^in/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/understand-tax', permanent=True),  # noqa
    ),
    url(
        r'^in/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/access-talent', permanent=True),
    ),
    url(
        r'^in/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^in/industries/($|index\.html$)',
        RedirectView.as_view(url='/industries', permanent=True),
    ),
    url(
        r'^in/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/industries/aerospace', permanent=True),
    ),
    url(
        r'^in/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^in/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^in/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^in/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/industries/retail', permanent=True),
    ),
    url(
        r'^in/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive', permanent=True),
    ),
    url(
        r'^in/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^in/industries/automotive/research-and-development/($|index\.html$)',
        RedirectView.as_view(
            url='/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^in/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^in/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy', permanent=True),
    ),
    url(
        r'^in/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^in/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^in/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^in/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^in/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/nuclear', permanent=True),
    ),
    url(
        r'^in/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/industries/health-and-life', permanent=True),  # noqa
    ),
    url(
        r'^in/industries/health-and-life/medical-technology/($|index\.html$)',
        RedirectView.as_view(
            url='/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^in/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^in/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative', permanent=True),
    ),
    url(
        r'^in/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative/content-and-production',
                             permanent=True),
    ),
    url(
        r'^in/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^in/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^in/industries/financial-services/asset-management/($|index\.html$)',
        RedirectView.as_view(
            url='/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^in/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^in/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/industries/technology', permanent=True),
    ),
    url(
        r'^in/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^in/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/terms-and-conditions', permanent=True),
    ),
    url(
        r'^in/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/privacy-policy', permanent=True),
    ),
    url(
        r'^in/feedback/($|index\.html$)',
        RedirectView.as_view(url='/feedback', permanent=True),
    ),
    url(
        r'^in/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^in/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/enquiries/error', permanent=True),
    ),
    url(
        r'^in/contact/($|index\.html$)',
        RedirectView.as_view(url='/contact', permanent=True),
    ),
    url(
        r'^in/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/location-guide', permanent=True),
    ),
    url(
        r'^in/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/location-guide/confirmation',
                             permanent=True),
    ),

    # us
    url(
        r'^us/($|index\.html$)',
        RedirectView.as_view(url='/', permanent=True),
    ),
    url(
        r'^us/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^us/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^us/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide', permanent=True),
    ),
    url(
        r'^us/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^us/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^us/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^us/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/how-to-setup', permanent=True),
    ),
    url(
        r'^us/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^us/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/access-talent', permanent=True),
    ),
    url(
        r'^us/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^us/industries/($|index\.html$)',
        RedirectView.as_view(url='/industries', permanent=True),
    ),
    url(
        r'^us/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/industries/aerospace', permanent=True),
    ),
    url(
        r'^us/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^us/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^us/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^us/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/industries/retail', permanent=True),
    ),
    url(
        r'^us/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive', permanent=True),
    ),
    url(
        r'^us/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^us/industries/automotive/research-and-development/($|index\.html$)',
        RedirectView.as_view(
            url='/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^us/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^us/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy', permanent=True),
    ),
    url(
        r'^us/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^us/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^us/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^us/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^us/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/nuclear', permanent=True),
    ),
    url(
        r'^us/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^us/industries/health-and-life/medical-technology/($|index\.html$)',
        RedirectView.as_view(
            url='/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^us/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^us/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative', permanent=True),
    ),
    url(
        r'^us/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative/content-and-production',
                             permanent=True),
    ),
    url(
        r'^us/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^us/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^us/industries/financial-services/asset-management/($|index\.html$)',
        RedirectView.as_view(
            url='/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^us/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^us/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/industries/technology', permanent=True),
    ),
    url(
        r'^us/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^us/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/terms-and-conditions', permanent=True),
    ),
    url(
        r'^us/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/privacy-policy', permanent=True),
    ),
    url(
        r'^us/feedback/($|index\.html$)',
        RedirectView.as_view(url='/feedback', permanent=True),
    ),
    url(
        r'^us/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^us/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/enquiries/error', permanent=True),
    ),
    url(
        r'^us/contact/($|index\.html$)',
        RedirectView.as_view(url='/contact', permanent=True),
    ),
    url(
        r'^us/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/location-guide', permanent=True),
    ),
    url(
        r'^us/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/location-guide/confirmation',
                             permanent=True),
    ),


    # int
    url(
        r'^int/($|index\.html$)',
        RedirectView.as_view(url='/', permanent=True),
    ),
    url(
        r'^int/404.html$',
        NotFoundView.as_view(),
    ),
    url(
        r'^int/500.html$',
        ServerErrorView.as_view(),
    ),
    url(
        r'^int/setup-guide/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide', permanent=True),
    ),
    url(
        r'^int/setup-guide/establish-address/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/establish-address',
                             permanent=True),
    ),
    url(
        r'^int/setup-guide/apply-for-visa/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/apply-for-visa',
                             permanent=True),
    ),
    url(
        r'^int/setup-guide/open-a-business-account/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/open-a-business-account',
                             permanent=True),
    ),
    url(
        r'^int/setup-guide/how-to-setup/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/how-to-setup', permanent=True),
    ),
    url(
        r'^int/setup-guide/understand-tax/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/understand-tax',
                             permanent=True),
    ),
    url(
        r'^int/setup-guide/access-talent/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/access-talent', permanent=True),
    ),
    url(
        r'^int/setup-guide/understand-legal/($|index\.html$)',
        RedirectView.as_view(url='/setup-guide/understand-legal',
                             permanent=True),
    ),
    url(
        r'^int/industries/($|index\.html$)',
        RedirectView.as_view(url='/industries', permanent=True),
    ),
    url(
        r'^int/industries/aerospace/($|index\.html$)',
        RedirectView.as_view(url='/industries/aerospace', permanent=True),
    ),
    url(
        r'^int/industries/advanced-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/industries/advanced-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/industries/food-and-drink-manufacturing/($|index\.html$)',
        RedirectView.as_view(url='/industries/food-and-drink-manufacturing',
                             permanent=True),
    ),
    url(
        r'^int/industries/food-and-drink-manufacturing/freefrom/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/food-and-drink-manufacturing/freefrom',
            permanent=True),
    ),
    url(
        r'^int/industries/retail/($|index\.html$)',
        RedirectView.as_view(url='/industries/retail', permanent=True),
    ),
    url(
        r'^int/industries/automotive/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive', permanent=True),
    ),
    url(
        r'^int/industries/automotive/motorsport/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive/motorsport',
                             permanent=True),
    ),
    url(
        r'^int/industries/automotive/research-and-development/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/automotive/research-and-development',
            permanent=True),
    ),
    url(
        r'^int/industries/automotive/supply-chain/($|index\.html$)',
        RedirectView.as_view(url='/industries/automotive/supply-chain',
                             permanent=True),
    ),
    url(
        r'^int/industries/energy/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy', permanent=True),
    ),
    url(
        r'^int/industries/energy/offshore-wind/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/offshore-wind',
                             permanent=True),
    ),
    url(
        r'^int/industries/energy/electrical-networks/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/electrical-networks',
                             permanent=True),
    ),
    url(
        r'^int/industries/energy/energy-from-waste/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/energy-from-waste',
                             permanent=True),
    ),
    url(
        r'^int/industries/energy/oil-and-gas/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/oil-and-gas',
                             permanent=True),
    ),
    url(
        r'^int/industries/energy/nuclear/($|index\.html$)',
        RedirectView.as_view(url='/industries/energy/nuclear', permanent=True),
    ),
    url(
        r'^int/industries/health-and-life/($|index\.html$)',
        RedirectView.as_view(url='/industries/health-and-life',
                             permanent=True),
    ),
    url(
        r'^int/industries/health-and-life/medical-technology/($|index\.html$)',
        RedirectView.as_view(
            url='/industries/health-and-life/medical-technology',
            permanent=True),
    ),
    url(
        r'^int/industries/health-and-life/pharmaceutical-manufacturing/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/health-and-life/pharmaceutical-manufacturing',
            permanent=True),
    ),
    url(
        r'^int/industries/creative/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative', permanent=True),
    ),
    url(
        r'^int/industries/creative/content-and-production/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative/content-and-production',
                             permanent=True),
    ),
    url(
        r'^int/industries/creative/digital-media/($|index\.html$)',
        RedirectView.as_view(url='/industries/creative/digital-media',
                             permanent=True),
    ),
    url(
        r'^int/industries/financial-services/($|index\.html$)',
        RedirectView.as_view(url='/industries/financial-services',
                             permanent=True),
    ),
    url(
        r'^int/industries/financial-services/asset-management/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/financial-services/asset-management',
            permanent=True),
    ),
    url(
        r'^int/industries/financial-services/financial-technology/($|index\.html$)',  # noqa
        RedirectView.as_view(
            url='/industries/financial-services/financial-technology',
            permanent=True),
    ),
    url(
        r'^int/industries/technology/($|index\.html$)',
        RedirectView.as_view(url='/industries/technology', permanent=True),
    ),
    url(
        r'^int/industries/technology/data-analytics/($|index\.html$)',
        RedirectView.as_view(url='/industries/technology/data-analytics',
                             permanent=True),
    ),
    url(
        r'^int/terms-and-conditions/($|index\.html$)',
        RedirectView.as_view(url='/terms-and-conditions', permanent=True),
    ),
    url(
        r'^int/privacy-policy/($|index\.html$)',
        RedirectView.as_view(url='/privacy-policy', permanent=True),
    ),
    url(
        r'^int/feedback/($|index\.html$)',
        RedirectView.as_view(url='/feedback', permanent=True),
    ),
    url(
        r'^int/enquiries/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/enquiries/confirmation', permanent=True),
    ),
    url(
        r'^int/enquiries/error/($|index\.html$)',
        RedirectView.as_view(url='/enquiries/error', permanent=True),
    ),
    url(
        r'^int/contact/($|index\.html$)',
        RedirectView.as_view(url='/contact', permanent=True),
    ),
    url(
        r'^int/location-guide/($|index\.html$)',
        RedirectView.as_view(url='/location-guide', permanent=True),
    ),
    url(
        r'^int/location-guide/confirmation/($|index\.html$)',
        RedirectView.as_view(url='/location-guide/confirmation',
                             permanent=True),
    ),
]
