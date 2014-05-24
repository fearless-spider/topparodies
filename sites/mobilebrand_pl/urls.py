from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from sitesngine.pages.views import MultiLanguagePageSitemap
from zinnia.sitemaps import TagSitemap, EntrySitemap, AuthorSitemap, CategorySitemap
from phantom import admin_site

admin.autodiscover()
admin_site._registry.update(admin.site._registry)

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,
            'pages':MultiLanguagePageSitemap,}

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin_site.urls)),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^elfinder/', include('elfinder.urls')),
    url(r'^', include('sitesngine.pages.urls')),
)