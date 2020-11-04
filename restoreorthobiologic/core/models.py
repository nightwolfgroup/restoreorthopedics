from blocks import blocks
from django.db import models
from django.shortcuts import render
from django.contrib import messages
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from autoslug import AutoSlugField
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtailmetadata.models import MetadataPageMixin
from wagtailmenus.models import AbstractMainMenuItem
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import StreamFieldPanel, TabbedInterface, ObjectList, FieldPanel, MultiFieldPanel


# Home Page ----------------------------------------------------------------------------------------------------------->
class HomePage(MetadataPageMixin, Page):
    template = 'frontend/index.html'
    max_count = 1
    hero = StreamField([
        ('title', blocks.ParallaxTitle())
    ])
    content = StreamField([
        ('services', blocks.ServiceCards()),
        ('testimonials', blocks.TestimonialCards()),
        ('CTA', blocks.CTABlock()),
        ('map', blocks.MapBlock()),
        ('FAQ', blocks.CardsWithFAQ()),
        ('latest_blog', blocks.LatestBlogPosts())
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
        verbose_name = 'Home Page'


# About Page ---------------------------------------------------------------------------------------------------------->
class AboutPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['core.HomePage']
    subpage_types = []
    template = 'frontend/generic.html'

    hero = StreamField([
        ('title', blocks.MissionStatementBlock())
    ])
    content = StreamField([
        ('doctor_spotlight', blocks.DoctorSpotlight()),
        ('testimonials', blocks.TestimonialIllustration()),
        ('cta', blocks.CTALogoBlock()),
        ('map', blocks.MapBlock())
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
        verbose_name = 'About Page'


# Testimonial Page ---------------------------------------------------------------------------------------------------->
class TestimonialPage(MetadataPageMixin, Page):
    """ Testimonial page utilizes Dr.com JavaScript plugin """
    max_count = 1
    parent_page_types = ['core.HomePage']
    subpage_types = []
    template = 'frontend/testimonial-page.html'

    class Meta:
        verbose_name = 'Testimonial Page'


# Contact Page & Message Model ---------------------------------------------------------------------------------------->
class Message(models.Model):
    """ Messages sent from the frontend of the website """
    first_name = models.CharField(
        max_length=30,
        blank=False
    )
    last_name = models.CharField(
        max_length=30,
        blank=False
    )
    email = models.EmailField(
        max_length=50,
        blank=False
    )
    phone_number = models.CharField(
        max_length=12,
        blank=False
    )
    message = models.TextField(
        max_length=2000,
        blank=False
    )
    staff_notes = models.TextField(
        blank=True,
        null=True,
        help_text='Internal notes for staff communication'
    )
    slug = AutoSlugField(
        populate_from='email'
    )
    viewed = models.BooleanField(default=False)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_on']

    def __str__(self):
        return self.first_name + ' ' + str(self.last_name)


class ContactPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['core.HomePage']
    subpage_types = []
    subtitle = models.CharField(
        max_length=255,
        blank=False,
        default='We will get back to you as soon as possible!'
    )
    background_image = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Background Image',
        related_name='background_image'
    )
    map_image = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Map Image',
        related_name='contact_map_image',
    )
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        ImageChooserPanel('background_image'),
        ImageChooserPanel('map_image')
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Page Content'),
        ObjectList(MetadataPageMixin.promote_panels, heading='SEO/Menu'),
        ObjectList(Page.settings_panels, heading='Page Settings', classname='settings')
    ])

    def serve(self, request):
        from core.forms import MessageForm
        # Valid form submission
        if request.method == 'POST':
            form = MessageForm(request.POST or None)
            if form.is_valid():
                # Save to database
                data = form.cleaned_data
                Message.objects.create(**data)
                # Send email to staff
                html_email = render_to_string('emails/staff-message.html', {'data': data})
                text_email = strip_tags(html_email)
                email = EmailMultiAlternatives(
                    f'New Message from {data["first_name"]} {data["last_name"]}',
                    text_email,
                    'Restore Orthopedics & Sports Medicine <donotreply@restoreorthobiologic.com>',
                    ['admin@restoreorthobiologic.com'],
                )
                email.attach_alternative(html_email, 'text/html')
                email.fail_silently = True
                email.send()
                # Reload page on successful submission
                form = MessageForm()
                messages.success(request, 'Your message has been received!')
                return render(request, 'form-pages/contact.html', {'form': form, 'self': self})
            else:
                # Reload page with error message if invalid
                messages.error(request, 'There seems to have been an error, '
                                        'please correct any missing or invalid fields.')
                return render(request, 'form-pages/contact.html', {'form': form, 'self': self})
        else:
            form = MessageForm()
            context = {'form': form, 'self': self}
            return render(request, 'form-pages/contact.html', context)

    class Meta:
        verbose_name = 'Contact Page'


# Legal Pages --------------------------------------------------------------------------------------------------------->
class LegalPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['core.HomePage']
    subpage_types = ['core.LegalPost']
    template = 'frontend/generic.html'

    hero = StreamField([
        ('title', blocks.TitleBlock())
    ])
    content = StreamField([
        ('cards', blocks.IconCardWithLink()),
        ('help', blocks.HelpBlock())
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
        verbose_name = 'Legal Home Page'


class LegalPost(MetadataPageMixin, Page):
    parent_page_types = ['core.LegalPage']
    subpage_types = []
    template = 'frontend/generic.html'

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    title_panels = Page.content_panels
    content = StreamField([
        ('legal_article', blocks.LegalBlock()),
    ])
    content_panels = [
        StreamFieldPanel('content'),
    ]
    edit_handler = TabbedInterface([
        ObjectList(title_panels, heading='Title & Header'),
        ObjectList(content_panels, heading='Page Content'),
        ObjectList(MetadataPageMixin.promote_panels, heading='SEO/Menu'),
        ObjectList(Page.settings_panels, heading='Page Settings', classname='settings')
    ])

    class Meta:
        verbose_name = 'Legal Policy'


# Global Settings ----------------------------------------------------------------------------------------------------->
@register_setting(icon='fa-facebook')
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        blank=True,
        null=True,
        help_text="Facebook URL",
        default='https://www.facebook.com/RestoreOrthopedics/'
    )
    twitter = models.URLField(
        blank=True,
        null=True,
        help_text="Twitter URL",
        default='https://twitter.com/OrthoSonora'
    )
    instagram = models.URLField(
        blank=True,
        null=True,
        help_text="Instagram URL",
        default='https://www.instagram.com/restoreorthobiologic/'
    )
    google = models.URLField(
        blank=True,
        null=True,
        help_text='Google Business URL',
        default='https://g.page/restoreorthosonora?gm'
    )
    youtube = models.URLField(
        blank=True,
        null=True,
        help_text="YouTube Channel URL",
        verbose_name='YouTube',
        default='https://www.youtube.com/channel/UCzw1usochiCFXobpi5omsoA'
    )
    panels = [
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('instagram'),
            FieldPanel('twitter'),
            FieldPanel('google'),
            FieldPanel('youtube'),
        ], heading='Social Media Accounts')
    ]

    class Meta:
        verbose_name = 'Social Media Accounts'


@register_setting(icon='fa-building-o')
class BusinessSettings(BaseSetting):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Name',
        default='Restore Orthopedics & Sports Medicine'
    )
    street_address = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Street',
        default='13949 Mono Way'
    )
    city = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='City',
        default='Sonora'
    )
    state = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        verbose_name='State',
        default='CA'
    )
    zip = models.CharField(
        max_length=5,
        blank=False,
        null=False,
        verbose_name='Zip',
        default='95370'
    )
    phone = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Phone',
        default='(209) 533-5371'
    )
    fax = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name='Fax',
        default='(209) 533-5372'
    )
    email = models.EmailField(
        blank=False,
        null=True,
        verbose_name='Email',
        default='admin@restoreorthobiologic.com'
    )
    sunday_hours = models.CharField(
        blank=False,
        max_length=20,
        default='Closed',
        verbose_name='Sunday',
    )
    monday_hours = models.CharField(
        blank=False,
        max_length=20,
        default='8:00 AM - 4:30 PM',
        verbose_name='Monday'
    )
    tuesday_hours = models.CharField(
        blank=False,
        max_length=20,
        default='8:00 AM - 4:30 PM',
        verbose_name='Tuesday'
    )
    wednesday_hours = models.CharField(
        blank=False,
        max_length=20,
        default='8:00 AM - 4:30 PM',
        verbose_name='Wednesday'
    )
    thursday_hours = models.CharField(
        blank=False,
        max_length=20,
        default='8:00 AM - 4:30 PM',
        verbose_name='Thursday'
    )
    friday_hours = models.CharField(
        blank=False,
        max_length=20,
        default='8:00 AM - 4:30 PM',
        verbose_name='Friday'
    )
    saturday_hours = models.CharField(
        blank=False,
        max_length=20,
        default='Closed',
        verbose_name='Saturday'
    )
    logo_light = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Main (light)',
        null=True,
        related_name='logo_light'
    )
    logo_dark = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Main (dark)',
        null=True,
        related_name='logo_dark'
    )
    logo_footer = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Footer',
        null=True,
        related_name='logo_footer'
    )
    logo_footer_alt = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Footer (alt)',
        null=True,
        related_name='logo_footer_alt'
    )
    logo_icon = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Icon',
        null=True,
        related_name='logo_icon'
    )
    logo_icon_footer = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Footer icon',
        null=True,
        related_name='logo_icon_footer'
    )
    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
        ], heading='Business Name'),
        MultiFieldPanel([
            FieldPanel('sunday_hours'),
            FieldPanel('monday_hours'),
            FieldPanel('tuesday_hours'),
            FieldPanel('wednesday_hours'),
            FieldPanel('thursday_hours'),
            FieldPanel('friday_hours'),
            FieldPanel('saturday_hours')
        ], heading='Business Hours',
            help_text='Define you business hours with this format: H:MM AM/PM - '
                      'H:MM AM/PM - If business is closed type "Closed"'
        ),
        MultiFieldPanel([
            FieldPanel('street_address'),
            FieldPanel('city'),
            FieldPanel('state'),
            FieldPanel('zip')
        ], heading='Business Address'),
        MultiFieldPanel([
            FieldPanel('phone'),
            FieldPanel('fax'),
            FieldPanel('email'),
        ], heading='Business Contact Information'),
        MultiFieldPanel([
            ImageChooserPanel('logo_light'),
            ImageChooserPanel('logo_dark'),
            ImageChooserPanel('logo_footer'),
            ImageChooserPanel('logo_footer_alt'),
            ImageChooserPanel('logo_icon'),
            ImageChooserPanel('logo_icon_footer')
        ], heading='Business Logo')
    ]

    def __str__(self):
        return 'Business Settings'
