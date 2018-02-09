from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        ImageChooserPanel('hero_image'),
    ]

    def get_context(self, request):
        # imports here, as otherwise a circular dependency can happen
        # during the initial migration
        from sector.models import SectorPage
        from setup_guide.models import SetupGuidePage
        context = super().get_context(request)
        context.update(
            sector_cards=SectorPage.objects.live(),
            setup_guide_cards=SetupGuidePage.objects.live(),
        )
        return context
