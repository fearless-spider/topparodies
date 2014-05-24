from django.conf.urls import patterns, url

from sitesngine.pages.views import details
from sitesngine.pages import settings


__author__ = 'fearless'  # "from birth till death"

if settings.SITESNGINE_PAGE_USE_LANGUAGE_PREFIX:
    urlpatterns = patterns('',
                           url(r'^(?P<lang>[-\w]+)/(?P<path>.*)$', details,
                               name='pages-details-by-path'),
                           # can be used to change the URL of the root page
                           #url(r'^$', details, name='pages-root'),
    )
else:
    urlpatterns = patterns('',
                           url(r'^(?P<path>.*)$', details, name='pages-details-by-path'),
                           # can be used to change the URL of the root page
                           #url(r'^$', details, name='pages-root'),
    )
