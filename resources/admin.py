from resources.models import AppointmentRequest
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register


class AppointmentRequestAdmin(ModelAdmin):
    model = AppointmentRequest
    menu_label = 'Appointment Requests'
    menu_icon = 'fa-calendar'
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'ideal_day',
        'appointment_type',
        'requested_on',
        'staff_notes',
        'viewed'
    )
    export_filename = 'appointment_requests'
    list_export = (
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'ideal_day',
        'appointment_type',
        'requested_on',
        'staff_notes',
        'message'
    )
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')


modeladmin_register(AppointmentRequestAdmin)
