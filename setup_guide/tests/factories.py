import factory.fuzzy
import wagtail_factories


class SetupGuidePageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = 'setup_guide.SetupGuidePage'

    description_en = factory.fuzzy.FuzzyText(length=255)
    heading_en = factory.fuzzy.FuzzyText(length=255)
    sub_heading_en = factory.fuzzy.FuzzyText(length=255)
    subsections_en = factory.fuzzy.FuzzyText(length=255)
    slug_en = factory.fuzzy.FuzzyText(length=10)
    slug = factory.fuzzy.FuzzyText(length=10)
    title = factory.fuzzy.FuzzyText(length=10)
    title_en = factory.fuzzy.FuzzyText(length=10)
    depth = 1
    live = True
    parent = None
