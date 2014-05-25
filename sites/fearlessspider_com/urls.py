from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from sitesngine.pages.views import MultiLanguagePageSitemap

admin.autodiscover()
#admin.site._registry.update(admin.site._registry)

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('syte.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^elfinder/', include('sitesngine.elfinder.urls')),
    url(r'^', include('sitesngine.pages.urls')),
)