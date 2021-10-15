from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList, StreamFieldPanel, RichTextFieldPanel, \
    InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin
from blocks import blocks
from io import BytesIO
from xhtml2pdf import pisa


# Resource Page ------------------------------------------------------------------------------------------------------->
class ResourcesPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['core.HomePage']
    subpage_types = [
        'resources.RequestAppointmentPage',
        'resources.OnboardingPage',
        'resources.EducationHomePage',
        'resources.EducationPage',
        'resources.FAQHomePage',
        'resources.FAQPage',
        'resources.FormsPage'
    ]
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
        verbose_name = 'Resources Home Page'


# Appointment Request Model & Page ------------------------------------------------------------------------------------>
class AppointmentRequest(models.Model):
    """ Model for appointment requests sent from the frontend of the website """
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
    ideal_day = models.CharField(
        max_length=10,
        blank=False,
    )
    appointment_type = models.CharField(
        max_length=50,
        blank=False,
    )
    message = models.TextField(
        max_length=2000,
        blank=True
    )
    staff_notes = models.TextField(
        blank=True,
        null=True,
        help_text='Internal notes for staff communication'
    )
    requested_on = models.DateTimeField(auto_now_add=True)
    captcha = models.TextField(blank=True, null=True)
    viewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-requested_on']

    def __str__(self):
        return self.first_name + ' ' + str(self.last_name)


class RequestAppointmentPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['resources.ResourcesPage']
    subpage_types = []
    subtitle = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional text displayed below the page title'
    )
    background_image = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Background Image',
        related_name='appointment_request_background'
    )
    map_image = models.ForeignKey(
        'wagtailimages.image',
        on_delete=models.PROTECT,
        verbose_name='Map Image',
        related_name='map_image'
    )
    # Wagtail admin interface configuration
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
        from resources.forms import AppointmentRequestForm

        if request.method == 'POST':
            form = AppointmentRequestForm(request.POST or None)
            if form.is_valid():
                data = form.cleaned_data
                AppointmentRequest.objects.create(**data)
                # Email message
                html_email = render_to_string('emails/staff-appointment-request.html', {'data': data})
                text_email = strip_tags(html_email)
                email = EmailMultiAlternatives(
                    f'Appointment Request: {data["first_name"]} {data["last_name"]}',
                    text_email,
                    'Restore Orthopedics & Sports Medicine <donotreply@restoreorthobiologic.com>',
                    ['admin@restoreorthobiologic.com'],
                )
                email.attach_alternative(html_email, 'text/html')
                email.fail_silently = True
                email.send()
                # Reload page on successful submission
                form = AppointmentRequestForm()
                messages.success(request, 'Your request has been received!')
                return render(request, 'form-pages/appointment-request.html', {'form': form, 'self': self})
            else:
                # Reload page with error message if invalid
                messages.error(request, 'There seems to have been an error, '
                                        'please correct any missing or invalid fields.')
                return render(request, 'form-pages/appointment-request.html', {'form': form, 'self': self})
        else:
            form = AppointmentRequestForm()
            return render(request, 'form-pages/appointment-request.html', {'form': form, 'self': self})

    class Meta:
        verbose_name = 'Appointment Request Page'


# Onboarding Page & PDF Render Function ------------------------------------------------------------------------------->
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class OnboardingPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['resources.ResourcesPage']
    subpage_types = []
    subtitle = models.CharField(
        max_length=255,
        blank=False,
    )
    # Wagtail admin interface configuration
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Page Content'),
        ObjectList(MetadataPageMixin.promote_panels, heading='SEO/Menu'),
        ObjectList(Page.settings_panels, heading='Page Settings', classname='settings')
    ])

    def serve(self, request):
        if request.method == 'POST':
            data = request.POST.dict()
            pdf = render_to_pdf('form-pages/onboarding-pdf-template.html', {'data': data})
            html_email = render_to_string('emails/staff-onboarding.html', {'data': data})
            text_email = strip_tags(html_email)
            email = EmailMultiAlternatives(
                'Intake Forms Submitted for Patient',
                text_email,
                'Restore Orthopedics & Sports Medicine <donotreply@restoreorthobiologic.com>',
                ['admin@restoreorthobiologic.com'],
            )
            email.attach_alternative(html_email, 'text/html')
            email.attach('onboarding.pdf', pdf.getvalue(), 'application/pdf')
            email.fail_silently = True
            email.send()
            messages.success(request, 'Onboarding Successful! Thank you for submitting your information.')
            return render(request, 'form-pages/onboarding.html', {'self': self})
        else:
            return render(request, 'form-pages/onboarding.html', {'self': self})

    class Meta:
        verbose_name = 'Onboarding Page'


# Education List & Detail Pages --------------------------------------------------------------------------------------->
class EducationHomePage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['resources.ResourcesPage']
    subpage_types = ['resources.EducationPage']
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
        verbose_name = 'Education List Page'


class EducationPage(MetadataPageMixin, Page):
    parent_page_types = ['resources.EducationHomePage']
    subpage_types = []
    template = 'frontend/generic.html'
    hero = StreamField([
        ('title', blocks.TitleBlock())
    ])
    content = StreamField([
        ('infographics', blocks.GalleryModalBlock()),
        ('ebooks', blocks.GalleryFileDownloadBlock()),
        ('videos', blocks.VideoShowcaseBlock()),
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
        verbose_name = 'Education Page'


# FAQ List & Detail Pages --------------------------------------------------------------------------------------------->
class FAQHomePage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['resources.ResourcesPage']
    subpage_types = ['resources.FAQPage']
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
        verbose_name = 'FAQ Home Page'


class FAQ(Orderable):
    page = ParentalKey('resources.FAQPage', related_name='frequent_questions')
    question = models.CharField(max_length=500, blank=False)
    answer = models.TextField(blank=False)
    panels = [
        FieldPanel('question'),
        RichTextFieldPanel('answer')
    ]


class RelatedArticles(Orderable):
    page = ParentalKey('resources.FAQPage', related_name='related_articles')
    related_article = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        PageChooserPanel('related_article'),
    ]


class FAQPage(MetadataPageMixin, Page):
    parent_page_types = ['resources.FAQHomePage']
    subpage_types = []
    template = 'frontend/faq-page.html'
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('related_articles', label='Related Article'),
        ], heading='Related Articles'),
        MultiFieldPanel([
            InlinePanel('frequent_questions', label='FAQ'),
        ], heading='Frequently Asked Questions')
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Page Content'),
        ObjectList(MetadataPageMixin.promote_panels, heading='SEO/Menu'),
        ObjectList(Page.settings_panels, heading='Page Settings', classname='settings')
    ])

    class Meta:
        verbose_name = 'FAQ Page'


# Forms Page ---------------------------------------------------------------------------------------------------------->
class FormsPage(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['resources.ResourcesPage']
    subpage_types = []
    template = 'frontend/generic.html'
    hero = StreamField([
        ('title', blocks.TitleBlock())
    ])
    content = StreamField([
        ('cards', blocks.PDFFormsBlock()),
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
        verbose_name = 'Patient Forms Page'
