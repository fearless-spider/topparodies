from .base import *

__author__ = 'fearless'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'www.topparodies.com',
    'topparodies.com',
]

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'topparodies',
        'PASSWORD': '',
        'USER': 'fearless',
        'PORT': '3306',
        'HOST': '127.0.0.1',
    },
}