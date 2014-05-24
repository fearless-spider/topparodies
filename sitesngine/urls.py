from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from sitesngine.hosts.views import SiteInfo
from sitesngine.pages.views import MultiLanguagePageSitemap
from zinnia.sitemaps import TagSitemap, EntrySitemap, AuthorSitemap, CategorySitemap

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitesngine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^site-info$', SiteInfo.as_view()),
    url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^elfinder/', include('sitesngine.elfinder.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,
            'pages':MultiLanguagePageSitemap,}

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

urlpatterns += patterns('',
    url(r'^', include('sitesngine.pages.urls')),
)