from django.contrib.auth.models import User
from django.db import models
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import StreamFieldPanel, TabbedInterface, ObjectList, FieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtailmetadata.models import MetadataPageMixin
from blocks import blocks


# Events Pages -------------------------------------------------------------------------------------------------------->
class Events(MetadataPageMixin, Page):
    max_count = 1
    parent_page_types = ['core.HomePage']
    subpage_types = ['events.EventPost']
    template = 'frontend/event-list.html'
    title_panels = Page.content_panels
    content_panels = [
        StreamFieldPanel('content'),
    ]
    edit_handler = TabbedInterface([
        ObjectList(title_panels, heading='Title & Header'),
        ObjectList(MetadataPageMixin.promote_panels, heading='SEO/Menu'),
        ObjectList(Page.settings_panels, heading='Page Settings', classname='settings')
    ])

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = EventPost.objects.live().public()
        return context

    class Meta:
        verbose_name = 'Events Home Page'


class EventPost(MetadataPageMixin, Page):
    parent_page_types = ['events.Events']
    subpage_types = []
    template = 'frontend/event.html'
    date = models.DateField(
        blank=False,
        help_text='Event Date'
    )
    time = models.TimeField(
        blank=False,
        help_text='Event Time'
    )
    location = models.CharField(
        blank=False,
        max_length=100,
        help_text='Event Location Title (ex: Continuum)'
    )
    location_address = models.CharField(
        blank=True,
        max_length=255,
        help_text='If virtual event, leave blank',
        verbose_name='Street Address'
    )
    location_city = models.CharField(
        blank=True,
        max_length=255,
        help_text='If virtual event, leave blank',
        verbose_name='City'
    )
    location_state = models.CharField(
        blank=True,
        max_length=50,
        help_text='If virtual event, leave blank',
        verbose_name='State'
    )
    hero = StreamField([
        ('event_title', blocks.EventTitle())
    ])
    content = StreamField([
        ('event_countdown', blocks.EventCountdown()),
        ('event_speakers', blocks.EventSpeakers()),
        ('call_to_action', blocks.EventCTA()),
        ('stats', blocks.EventStats()),
        ('schedule', blocks.EventSchedule()),
        ('location', blocks.EventLocation()),
        ('tickets', blocks.EventTickets())
    ])
    event_details = [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('time')
        ], heading='Event Date & Time'),
        MultiFieldPanel([
            FieldPanel('location'),
            FieldPanel('location_address'),
            FieldPanel('location_city'),
            FieldPanel('location_state')
        ], heading='Event Location')
    ]
    title_panels = Page.content_panels + [
        StreamFieldPanel('hero')
    ]
    content_panels = [
        StreamFieldPanel('content')
    ]
    edit_handler = TabbedInterface([
        ObjectList(title_panels, heading='Event Title & Header'),
        ObjectList(event_details, heading='Event Details'),
        ObjectList(content_panels, heading='Page Content'),
        ObjectList(MetadataPageMixin.promote_panels, heading='SEO/Menu'),
        ObjectList(Page.settings_panels, heading='Page Settings', classname='settings')
    ])

    class Meta:
        verbose_name = 'Event'
