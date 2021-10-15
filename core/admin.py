from core.snippets import Testimonial
from core.models import Message
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register


class TestimonialAdmin(ModelAdmin):
    model = Testimonial
    menu_label = 'Testimonials'
    menu_icon = 'fa-quote-right'
    menu_order = 103
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('quote', 'name')


modeladmin_register(TestimonialAdmin)


class MessageAdmin(ModelAdmin):
    model = Message
    menu_label = 'Messages'
    menu_icon = 'fa-comments'
    menu_order = 101
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'sent_on')
    search_fields = ('phone_number', 'email')
    export_filename = 'website_messages'
    list_export = (
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'sent_on'
    )


modeladmin_register(MessageAdmin)
