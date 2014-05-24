from django.contrib.sites.managers import CurrentSiteManager as DjangoCSM
from sitesngine.hosts.utils import current_site_id

__author__ = 'fearless' # "from birth till death"


class CurrentSiteManager(DjangoCSM):
    """
    Extends Django's site manager to first look up site by ID stored in
    the request, the session, then domain for the current request
    (accessible via threadlocals in ``sitesngine.hosts.request``), the
    environment variable ``SITESNGINE_SITE_ID`` (which can be used by
    management commands with the ``--site`` arg, finally falling back
    to ``settings.SITE_ID`` if none of those match a site.
    """
    def __init__(self, field_name=None, *args, **kwargs):
        super(DjangoCSM, self).__init__(*args, **kwargs)
        self.__field_name = field_name
        self.__is_validated = False

    def get_query_set(self):
        if not self.__is_validated:
            self._validate_field_name()
        lookup = {self.__field_name + "__id__exact": current_site_id()}
        return super(DjangoCSM, self).get_query_set().filter(**lookup)