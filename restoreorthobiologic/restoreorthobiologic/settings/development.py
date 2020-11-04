"""
Django Development Settings for the Restore Orthopedics & Sports Medicine Website
Django version: 3.1.2
Release: 2.0 (Addition of Wagtail CMS)
"""

from restoreorthobiologic.settings.common import *

DEBUG = True

SECRET_KEY = '*****'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'restoreorthobiologic/static'
]

# Media files (User uploaded content)
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


# ReCAPTCHA Keys
RECAPTCHA_PUBLIC_KEY = '******'
RECAPTCHA_PRIVATE_KEY = '******'


# Wagtail Google Analytics Dashboard
GA_KEY_FILEPATH = BASE_DIR / '******'
GA_VIEW_ID = '******'


# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '******'
EMAIL_HOST_PASSWORD = '******'
EMAIL_HOST_USER = '******'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
