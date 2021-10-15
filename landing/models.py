from wagtail.admin.edit_handlers import StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtailmetadata.models import MetadataPageMixin
from blocks import blocks


class LandingPage(MetadataPageMixin, Page):
    parent_page_types = ['core.HomePage']
    subpage_types = []
    template = 'frontend/generic.html'

    hero = StreamField([
        ('title1', blocks.TitleBlock()),
        ('title2', blocks.TitleWithCard()),
        ('title3', blocks.CarouselTitle()),
    ])
    content = StreamField([
        ('cta1', blocks.CTABlock()),
        ('cta2', blocks.CTALogoBlock()),
        ('map', blocks.MapBlock()),
        ('jarallax', blocks.JarallaxImage()),
        ('hotspots', blocks.HotspotsBlock()),
        ('icons', blocks.IconList()),
        ('help', blocks.HelpBlock()),
        ('modal_gallery', blocks.GalleryModalBlock()),
        ('modal_download', blocks.GalleryFileDownloadBlock()),
        ('video_showcase', blocks.VideoShowcaseBlock()),
        ('image_or_video', blocks.ImageIconList()),
        ('testimonial1', blocks.TestimonialCards()),
        ('testimonial2', blocks.TestimonialIllustration()),
        ('testimonial3', blocks.FeaturedTestimonials()),
        ('faq_cards', blocks.CardsWithFAQ()),
    ])
    title_panels = Page.content_panels + [
        StreamFieldPanel('hero')
    ]
    content_panels = [
        StreamFieldPanel('content')
    ]
    edit_handler = TabbedInterface([
        ObjectList(title_panels, heading='Title & Header'),
        ObjectList(content_panels, heading='Page Content'),
        ObjectList(MetadataPageMixin.promote_panels, heading='SEO/Menu'),
        ObjectList(Page.settings_panels, heading='Page Settings', classname='settings')
    ])

    class Meta:
        verbose_name = 'Landing Page'
