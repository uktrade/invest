import factory
import wagtail

from setup_guide.tests.factories import SetupGuidePageFactory


class RedirectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = wagtail.contrib.redirects.models.Redirect
        django_get_or_create = ('old_path',)

    redirect_page = factory.SubFactory(SetupGuidePageFactory)
