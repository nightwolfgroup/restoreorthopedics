from django.forms import forms, CharField, TextInput, EmailField, EmailInput, Textarea
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


class MessageForm(forms.Form):
    first_name = CharField(
        required=True,
        max_length=30,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
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
            }
        )
    )
    message = CharField(
        required=True,
        max_length=2000,
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4
            }
        )
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
