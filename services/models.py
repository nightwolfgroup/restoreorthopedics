from wagtail.admin.edit_handlers import StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtailmetadata.models import MetadataPageMixin
from blocks import blocks


# Services Page ------------------------------------------------------------------------------------------------------->
class ServicesPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['core.HomePage']
    subpage_types = ['services.ServicePage']
    template = 'frontend/generic.html'
    hero = StreamField([
        ('title', blocks.ServicesTitleBlock())
    ])
    content = StreamField([
        ('cta', blocks.CTALogoBlock()),
        ('testimonials', blocks.TestimonialIllustration())
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
        verbose_name = 'Services Home Page'


class ServicePage(MetadataPageMixin, Page):
    parent_page_types = ['services.ServicesPage']
    subpage_types = []
    template = 'frontend/generic.html'
    hero = StreamField([
        ('parallax_title', blocks.ParallaxTitleCard()),
        ('title', blocks.TitleWithCard()),
        ('carousel', blocks.CarouselTitle())
    ])
    content = StreamField([
        ('jarallax_image', blocks.JarallaxImage()),
        ('hotspots', blocks.HotspotsBlock()),
        ('icon_list', blocks.IconList()),
        ('cta', blocks.CTALogoBlock()),
        ('cta_2', blocks.CTABlock()),
        ('featured_testimonial', blocks.FeaturedTestimonials()),
        ('testimonials', blocks.TestimonialCards()),
        ('image_icon_list', blocks.ImageIconList())
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
        verbose_name = 'Service Page'
