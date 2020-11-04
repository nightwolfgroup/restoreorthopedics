"""
Django Settings for the Restore Orthopedics & Sports Medicine Website
Django version: 3.1.2
Release: 2.0 (Addition of Wagtail CMS)
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '******'

DEBUG = False

ALLOWED_HOSTS = ['restoreorthobiologic.com', 'www.restoreorthobiologic.com']

INSTALLED_APPS = [
    # Wagtail applications
    'wagtail.contrib.settings',
    'wagtail.contrib.forms',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.sitemaps',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'dashboard.apps.DashboardConfig',
    'wagtail.admin',
    'wagtail.core',
    # Third-party applications
    'modelcluster',
    'taggit',
    'wagtailmetadata',
    'wagalytics',
    'autoslug',
    'wagtailfontawesome',
    'wagtailmenus',
    'captcha',
    'wagtailstreamforms',
    # Django applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # Project-specific applications
    'blocks.apps.BlocksConfig',
    'blog.apps.BlogConfig',
    'careers.apps.CareersConfig',
    'core.apps.CoreConfig',
    'events.apps.EventsConfig',
    'landing.apps.LandingConfig',
    'resources.apps.ResourcesConfig',
    'services.apps.ServicesConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',

]

ROOT_URLCONF = 'restoreorthobiologic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/opt/restoreorthobiologic/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'restoreorthobiologic.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '******',
        'USER': '******',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/cache/restoreorthobiologic/cache/'
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = '/var/cache/restoreorthobiologic/static/'


# Media files (User uploaded content)
MEDIA_ROOT = '/var/opt/restoreorthobiologic/media/'
MEDIA_URL = '/media/'


# Messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.WARNING: 'warning',
    messages.INFO: 'info',
    messages.SUCCESS: 'success'
}


# Wagtail CMS Configuration
WAGTAILDOCS_SERVE_METHOD = 'direct'
WAGTAIL_SITE_NAME = 'Restore Orthopedics & Sports Medicine'
PASSWORD_REQUIRED_TEMPLATE = 'frontend/password-required.html'
WAGTAIL_FRONTEND_LOGIN_TEMPLATE = 'login.html'


# Wagtail StreamForms
WAGTAILSTREAMFORMS_FORM_TEMPLATES = (
    ('streamforms/form_block.html', 'Default Form Template'),
    ('form-pages/modal-form.html', 'Modal Form'),
)


# ReCAPTCHA Keys
RECAPTCHA_PUBLIC_KEY = '******'
RECAPTCHA_PRIVATE_KEY = '******'


# Wagtail Google Analytics Dashboard
GA_KEY_FILEPATH = '******'
GA_VIEW_ID = '******'


# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '******'
EMAIL_HOST_PASSWORD = '******'
EMAIL_HOST_USER = 'apikey'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SERVER_EMAIL = 'Restore Orthopedics & Sports Medicine <******>'
DEFAULT_FROM_EMAIL = 'Restore Orthopedics & Sports Medicine <******>'

ADMINS = [
    ('Nightwolf Group', 'admin@nightwolfgroup.com'),
]
MANAGERS = ADMINS


# Error/Debug Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            'class': 'logging.handlers.'
                     'TimedRotatingFileHandler',
            'filename': '/var/log/restoreorthobiologic/'
                        'restoreorthobiologic-django.log',
            'when': 'midnight',
            'backupCount': 60,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'root': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    }
}