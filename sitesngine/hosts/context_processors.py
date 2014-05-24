from django.conf import settings
from django.contrib.sites.models import Site

__author__ = 'fearless' # "from birth till death"


def current_site(request):
    site = Site.objects.get_current()
    return (settings.SITE_ID) and {'site': site} or {}