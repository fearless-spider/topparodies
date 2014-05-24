from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from parodies.models import Video
from parodies.views import IndexView, PrivacyView, TermsView, VideoDetail, TodayVideoListView, ThisWeekVideoListView, ThisMonthVideoListView, GroupVideoListView, TopVideoListView, LatestVideoListView
from phantom import admin_site

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'today', 'this_week', 'this_month']

    def location(self, item):
        return reverse(item)


class GroupViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return         [
            'bieber',
            'rihanna',
            'iphone',
            'google',
            'samsung',
            'duty',
            'minecraft',
            'lost',
            '300',
            'minaj',
            'direction',
            'gangnam',
            'miserables',
            'wars',
            'daft',
            'avengers',
            'superman',
            'ipad',
            'windows',
            'gta',
            'halo',
            'spiderman',
            'beyonce',
            'gaga',
            'obama',
            'porn',
        ]


    def location(self, item):
        return reverse('group_video', args=[item])

admin.autodiscover()
admin_site._registry.update(admin.site._registry)

info_dict = {
    'queryset': Video.objects.exclude(slug=''),
    'date_field': 'published_on',
}

sitemaps = {
    'parodies': GenericSitemap(info_dict, priority=0.6),
    'static': StaticViewSitemap,
    'group': GroupViewSitemap
}

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^privacy/$', PrivacyView.as_view(),name='privacy'),
    url(r'^terms/$', TermsView.as_view(),name='terms'),

    url(r'^parody/(?P<slug>[-_\w]+)/(?P<pk>\d+)$', VideoDetail.as_view(),name='video_detail'),
    url(r'^top$',TopVideoListView.as_view(),name='top'),
    url(r'^latest$',LatestVideoListView.as_view(),name='latest'),
    url(r'^today$',TodayVideoListView.as_view(),name='today'),
    url(r'^this_week$',ThisWeekVideoListView.as_view(),name='this_week'),
    url(r'^this_month$',ThisMonthVideoListView.as_view(),name='this_month'),
    url(r'^group/(?P<slug>[-_\w]+)$',GroupVideoListView.as_view(),name='group_video'),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /site_media/", mimetype="text/plain")),
	url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    url(r'^blog/', include('zinnia.urls')),
)