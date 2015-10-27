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
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'www.topparodies.com',
    'topparodies.com',
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
    'syte',
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

ROOT_URLCONF = 'topparodies.urls'

WSGI_APPLICATION = 'topparodies.wsgi.application'

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
    "syte.context_processor.site_pages",
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'topparodies',
        'PASSWORD': '13freakk5',
        'USER': 'root',
        'PORT': '3306',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'init_command': 'SET storage_engine=MyISAM',
        }
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
import os
import os.path

#try:
#    import dj_database_url
#    try: # python 2.x
#        from urllib import unquote
#    except ImportError: # python 3.x
#        from urllib.parse import unquote
#except ImportError:
#    pass
#else:
#    try:
#        with open(os.environ['DATABASE_PATH_SITESNGINE'], 'r') as url_file:
#            url = url_file.read()
#    except (IOError, KeyError):
#        pass
#    else:
#        DATABASES['default'] = dj_database_url.parse(url)
#        if DATABASES['default'].get('PASSWORD'):
#            DATABASES['default']['PASSWORD'] = unquote(DATABASES['default']['PASSWORD'])

SITES_DIR = os.path.join(os.path.dirname(__file__), '..', 'sites').replace('\\','/')
SITES_PACKAGE = 'sites'
DEFAULT_HOST = 'topparodies.com'
HOSTNAME_REDIRECTS = {
    'topparodies.com': 'www.topparodies.com',
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

from sitesngine.elfinder.utils.accesscontrol import fs_standard_access
ELFINDER_CONNECTOR_OPTION_SETS = {
    'pdf' : {
        'roots' : [
                   {
                   'id' : 'pdfset',
                   'driver' : 'elfinder.volumes.filesystem.ElfinderVolumeLocalFileSystem',
                   'path' : os.path.join(STATIC_ROOT, 'pdf'),
                   'alias' : 'PDF only',
                   'URL' : '%spdf/' % STATIC_URL,
                   'onlyMimes' : ['application/pdf',],
                   'uploadAllow' : ['application/pdf',],
                   'uploadDeny' : ['all',],
                   'uploadMaxSize' : '128m',
                   'disabled' : ['mkfile', 'archive'],
                   'accessControl' : fs_standard_access,
                   'attributes' : [
                                   {
                                   'pattern' : r'\.tmb$',
                                   'read' : True,
                                   'write': True,
                                   'hidden' : True,
                                   'locked' : True
                                   },
                                   ],
                   }
                   ]
}
}

ELFINDER_TINYMCE_PATH_TO_POPUP_JS = STATIC_URL + 'tiny_mce/tiny_mce_popup.js'

from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS

USE_TINYMCE = True

# -*- coding: utf-8 -*-
DEPLOYMENT_MODE = 'dev'
COMPRESS_REVISION_NUMBER = '1.0'

BLOG_PLATFORM = 'tumblr'  # Wordpress or tumblr

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'fearlessspider.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'rDjHObC8MGIN4HnpYyQhEkEMowLD9Lby0uRPZGUTVCabLhX910'

#Blog Integration: Wordpress
WORDPRESS_BLOG_URL = '[ENTER WORDPRESS BLOG URL] ex. gordonkoo.wordpress.com'
WORDPRESS_API_URL = 'https://public-api.wordpress.com/rest/v1/sites/{0}'.format(WORDPRESS_BLOG_URL)

#Tent.io Integration
TENT_INTEGRATION_ENABLED = False
TENT_ENTITY_URI = '[ENTER YOUR ENTITY URI HERE] ex. https://yourname.tent.is'
TENT_FEED_URL = '[ENTER A URL TO YOUR FEED] ex. https://yourname.tent.is'

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = False
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = '[ENTER TWITTER CONSUMER KEY HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_CONSUMER_SECRET = '[ENTER TWITTER CONSUMER SECRET HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_USER_KEY = '[ENTER TWITTER USER KEY HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_USER_SECRET = '[ENTER TWITTER USER SECRET HERE, SEE TWITTER SETUP INSTRUCTIONS]'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '[ENTER GITHUB ACCESS TOKEN HERE, SEE GITHUB SETUP INSTRUCTIONS]'

GITHUB_OAUTH_ENABLED = False
GITHUB_CLIENT_ID = '[ENTER GITHUB CLIENT ID HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_CLIENT_SECRET = '[ENTER GITHUB CLIENT SECRET HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Stack Overflow Integration
STACKOVERFLOW_INTEGRATION_ENABLED = False
STACKOVERFLOW_API_URL = 'http://api.stackoverflow.com/1.1/'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = False
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '[ENTER INSTAGRAM ACCESS TOKEN HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_USER_ID = '[ENTER INSTAGRAM USER_ID HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = '[ENTER INSTAGRAM CLIENT_ID HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_CLIENT_SECRET = '[ENTER INSTAGRAM CLIENT_SECRET HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = False
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = '[ENTER FOURSQUARE ACCESS TOKEN HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = False
FOURSQUARE_CLIENT_ID = '[ENTER FOURSQUARE CLIENT_ID HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_CLIENT_SECRET = '[ENTER FOURSQUARE CLIENT_SECRET HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#ShareThis
SHARETHIS_PUBLISHER_KEY = ''


#Woopra
WOOPRA_TRACKING_DOMAIN = ''
WOOPRA_TRACKING_IDLE_TIMEOUT = 300000  # 5 minutes
WOOPRA_TRACKING_INCLUDE_QUERY = False


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = ''


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = False
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = '[ENTER LASTFM API_KEY HERE, SEE LASTFM SETUP INSTRUCTIONS]'

#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = False
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = '[ENTER SOUNDCLOUD APPLICATION CLIENT_ID HERE]'
SOUNDCLOUD_SHOW_ARTWORK = False
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = False
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False

#Steam Integration
STEAM_INTEGRATION_ENABLED = True
STEAM_API_URL = 'http://api.steampowered.com/ISteamUser'
STEAM_API_KEY = 'E0843DEC51F926FF8051BE08A9F52FC5'


#Flickr Integration
FLICKR_INTEGRATION_ENABLED = False
FLICKR_ID = '[ENTER YOUR FLICKR ID (NOT USERNAME) HERE]' # You do your username->ID lookup here: http://idgettr.com/

#LinkedIn Integration
LINKEDIN_INTEGRATION_ENABLED = False
LINKEDIN_CONSUMER_KEY = '[ENTER YOUR LINKEDIN CONSUMER KEY HERE]'
LINKEDIN_CONSUMER_SECRET = '[ENTER YOUR LINKEDIN CONSUMER SECRET KEY HERE]'
LINKEDIN_USER_TOKEN = '[ENTER YOUR LINKED IN USER TOKEN HERE]'
LINKEDIN_USER_SECRET = '[ENTER YOUR LINKED IN USER SECRET HERE]'

SITEMAP_ENABLED = True
SITE_ROOT_URI = 'http://www.fearlessspider.com'
#RSS Feed Integration: (by default use Tumblr rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)
