from django.forms import forms, CharField, TextInput, EmailField, EmailInput, Select, Textarea
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from resources.choices import WEEK_DAY_CHOICES, APPOINTMENT_TYPE_CHOICES


class AppointmentRequestForm(forms.Form):
    first_name = CharField(
        required=True,
        max_length=30,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }
        )
    )
    last_name = CharField(
        required=True,
        max_length=30,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        )
    )
    email = EmailField(
        required=True,
        max_length=30,
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    phone_number = CharField(
        required=True,
        max_length=12,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '555-555-5555',
                'data-format': 'custom',
                'data-delimiter': '-',
                'data-blocks': '3 3 4',
                'maxlength': '12',
                'minlength': '12',
                'type': 'tel'
            }
        )
    )
    ideal_day = CharField(
        required=True,
        widget=Select(
            choices=WEEK_DAY_CHOICES,
            attrs={
                'class': 'form-control custom-select'
            }
        )
    )
    appointment_type = CharField(
        required=True,
        widget=Select(
            choices=APPOINTMENT_TYPE_CHOICES,
            attrs={
                'class': 'form-control custom-select'
            }
        )
    )
    message = CharField(
        required=True,
        max_length=2000,
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'rows': 5
            }
        )
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
