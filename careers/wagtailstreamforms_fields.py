from captcha.fields import ReCaptchaField
from django import forms
from wagtail.core import blocks
from wagtailstreamforms.fields import BaseField, register


@register('singleline')
class SingleLineTextField(BaseField):
    field_class = forms.CharField
    widget = forms.widgets.TextInput(attrs={'class': 'form-control'})

    def get_options(self, block_value):
        options = super().get_options(block_value)
        options.update({'max_length': block_value.get('max_length')})
        return options

    def get_form_block(self):
        return blocks.StructBlock([
            ('label', blocks.CharBlock()),
            ('help_text', blocks.CharBlock(required=False)),
            ('max_length', blocks.IntegerBlock(required=True)),
            ('required', blocks.BooleanBlock(required=False)),
        ], icon=self.icon, label=self.label)


@register('phone')
class PhoneNumberField(BaseField):
    field_class = forms.CharField
    widget = forms.widgets.TextInput(
        attrs={
            'class': 'form-control',
            'data-format': 'custom',
            'data-delimiter': '-',
            'data-blocks': '3 3 4',
            'placeholder': '555-555-5555',
            'maxlength': '12',
            'minlength': '12',
            'type': 'tel'
        }
    )

    def get_form_block(self):
        return blocks.StructBlock([
            ('label', blocks.CharBlock()),
            ('help_text', blocks.CharBlock(required=False)),
            ('required', blocks.BooleanBlock(required=False)),
        ], icon='fa-phone', label='Phone Number')


@register('email')
class EmailField(BaseField):
    field_class = forms.EmailField
    widget = forms.widgets.EmailInput(
        attrs={
            'class': 'form-control',
            'type': 'email'
        }
    )

    def get_form_block(self):
        return blocks.StructBlock([
            ('label', blocks.CharBlock()),
            ('help_text', blocks.CharBlock(required=False)),
            ('required', blocks.BooleanBlock(required=False)),
        ], icon='fa-at', label=self.label)


@register('date')
class DateField(BaseField):
    field_class = forms.DateField
    widget = forms.widgets.TextInput(attrs={'class': 'form-control appended-form-control cs-date-picker'})


@register('multiline')
class MultiLineTextField(BaseField):
    field_class = forms.CharField
    widget = forms.widgets.Textarea(attrs={'rows': 10, 'class': 'form-control'})


@register('recaptcha')
class ReCaptchaField(BaseField):
    field_class = ReCaptchaField
    icon = 'success'
    label = 'ReCAPTCHA field'

    def get_options(self, block_value):
        options = super().get_options(block_value)
        options.update({
            'required': True
        })
        return options

    def get_form_block(self):
        return blocks.StructBlock([
            ('label', blocks.CharBlock()),
            ('help_text', blocks.CharBlock(required=False)),
        ], icon=self.icon, label=self.label)
