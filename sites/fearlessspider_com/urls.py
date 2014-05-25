from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from sitesngine.pages.views import MultiLanguagePageSitemap

admin.autodiscover()
#admin.site._registry.update(admin.site._registry)

urlpatterns = patterns('',
    url(r'^', include('syte.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)