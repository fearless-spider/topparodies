"""Context processors for Page CMS."""
from sitesngine.pages import settings
from sitesngine.pages.models import Page


def media(request):
    """Adds media-related variables to the `context`."""
    return {
        'SITESNGINE_PAGES_MEDIA_URL': settings.SITESNGINE_PAGES_MEDIA_URL,
        'SITESNGINE_PAGE_USE_SITE_ID': settings.SITESNGINE_PAGE_USE_SITE_ID,
        'SITESNGINE_PAGE_HIDE_SITES': settings.SITESNGINE_PAGE_HIDE_SITES,
        'SITESNGINE_PAGE_LANGUAGES': settings.SITESNGINE_PAGE_LANGUAGES,
    }
