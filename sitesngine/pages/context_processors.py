"""Context processors for Django Sites N-gine Pages."""
from sitesngine.pages import settings
from sitesngine.pages.models import Page

__author__ = 'fearless'  # "from birth till death"


def media(request):
    """Adds media-related variables to the `context`."""
    return {
        'SITESNGINE_PAGES_MEDIA_URL': settings.SITESNGINE_PAGES_MEDIA_URL,
        'SITESNGINE_PAGE_USE_SITE_ID': settings.SITESNGINE_PAGE_USE_SITE_ID,
        'SITESNGINE_PAGE_HIDE_SITES': settings.SITESNGINE_PAGE_HIDE_SITES,
        'SITESNGINE_PAGE_LANGUAGES': settings.SITESNGINE_PAGE_LANGUAGES,
    }


def pages_navigation(request):
    """Adds essential pages variables to the `context`."""
    pages = Page.objects.navigation().order_by("tree_id")
    return {
        'pages_navigation': pages,
        'current_page': None
    }
