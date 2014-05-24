from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import Site
from django.conf import settings
from django.views.generic import View

__author__ = 'fearless' # "from birth till death"


class SiteInfo(View):
    def get(self, request):
        site = None
        if settings.SITE_ID:
            site = Site.objects.get_current()
        args = {
            'request_get_host':request.get_host(),
            'http_host':request.META['HTTP_HOST'],
            'site':site
        }
        return render_to_response('sitesngine/site_info.html', args, context_instance=RequestContext(request))