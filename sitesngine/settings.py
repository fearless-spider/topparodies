"""
Django settings for sitesngine project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# This is defined here as a do-nothing function because we can't import
# django.utils.translation -- that module depends on the settings.
gettext_noop = lambda s: s

# here is all the languages supported by the CMS
SITESNGINE_PAGE_LANGUAGES = (
    ('pl', gettext_noop('Polish')),
    ('en-us', gettext_noop('US English')),
)

# copy PAGE_LANGUAGES
languages = list(SITESNGINE_PAGE_LANGUAGES)

# redefine the LANGUAGES setting in order to be sure to have the correct request.LANGUAGE_CODE
LANGUAGES = languages

SITESNGINE_PAGE_USE_SITE_ID = True
SITE_ID = 1


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!g&ebi%&pu$3fmh_@aax#*tnn0)$fom#yay8u!3+93z721qby6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'sitesngine.megiteam.pl',
    'www.sitesngine.megiteam.pl',
    'www.topparodies.com',
    'topparodies.com',
    'www.mobilebrand.pl',
    'mobilebrand.pl',
    'www.fearlessspider.com',
    'fearlessspider.com',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'sites.topparodies_com',
    'sites.mobilebrand_pl',
    'sitesngine.hosts',
    'mptt',
    'sitesngine.elfinder',
    'tagging',
    'sitesngine.pages',
    'tinymce',
    'json_field',
    'django_pygments',
    'zinnia',
    'django_xmlrpc',
    'parodies',
    'south',
)

MIDDLEWARE_CLASSES = (
    'sitesngine.hosts.middleware.HostsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sitesngine.middleware.XForwardedForMiddleware',
    'sitesngine.hosts.request.CurrentRequestMiddleware',
    'sitesngine.hosts.middleware.AdminLoginInterfaceSelectorMiddleware',
    'sitesngine.hosts.middleware.SitePermissionMiddleware',
)

ROOT_URLCONF = 'sitesngine.urls'

WSGI_APPLICATION = 'sitesngine.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "sitesngine.hosts.context_processors.current_site",
    "sitesngine.pages.context_processors.media",
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
import os
import os.path

try:
    import dj_database_url
    try: # python 2.x
        from urllib import unquote
    except ImportError: # python 3.x
        from urllib.parse import unquote
except ImportError:
    pass
else:
    try:
        with open(os.environ['DATABASE_PATH_SITESNGINE'], 'r') as url_file:
            url = url_file.read()
    except (IOError, KeyError):
        pass
    else:
        DATABASES['default'] = dj_database_url.parse(url)
        if DATABASES['default'].get('PASSWORD'):
            DATABASES['default']['PASSWORD'] = unquote(DATABASES['default']['PASSWORD'])

SITES_DIR = os.path.join(os.path.dirname(__file__), '..', 'sites').replace('\\','/')
SITES_PACKAGE = 'sites'
DEFAULT_HOST = 'sitesngine.megiteam.pl'
HOSTNAME_REDIRECTS = {
    'mobilebrand.pl': 'www.mobilebrand.pl',
}
#ENV_HOSTNAMES = {
#    'django':    'djangoaaa',
#}
#SITES_FILTER = {'domain__endswith':'.example.com'}

FILE_UPLOAD_PERMISSIONS = 0644

SITESNGINE_PAGE_DEFAULT_TEMPLATE = 'pages/index.html'

SITESNGINE_PAGE_TAGGING = True

SITESNGINE_PAGE_HIDE_SITES = True

SITESNGINE_PAGE_TEMPLATES = (
    ('pages/index.html', 'Simple'),
    ('pages/page.html', 'Page'),
    ('pages/contact.html', 'Contact'),
)

SITESNGINE_PAGE_TINYMCE = True

ELFINDER_TINYMCE_PATH_TO_POPUP_JS = STATIC_URL + 'tiny_mce/tiny_mce_popup.js'

from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS

USE_TINYMCE = True
