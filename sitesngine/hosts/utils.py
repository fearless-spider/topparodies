import os
from django.conf import settings
from django.contrib.sites.models import Site
from sitesngine.hosts.request import current_request

__author__ = 'fearless'  # "from birth till death"


def make_tls_property(default=None):
    """Creates a class-wide instance property with a thread-specific value."""

    class TLSProperty(object):
        def __init__(self):
            from threading import local

            self.local = local()

        def __get__(self, instance, cls):
            if not instance:
                return self
            return self.value

        def __set__(self, instance, value):
            self.value = value

        def _get_value(self):
            return getattr(self.local, 'value', default)

        def _set_value(self, value):
            self.local.value = value

        value = property(_get_value, _set_value)

    return TLSProperty()


def has_site_permission(user):
    mw = "sitesngine.hosts.middleware.SitePermissionMiddleware"
    if mw not in settings.MIDDLEWARE_CLASSES:
        from warnings import warn

        warn(mw + " missing from settings.MIDDLEWARE_CLASSES - per site"
                  "permissions not applied")
        return user.is_staff and user.is_active
    return getattr(user, "has_site_permission", False)


def current_site_id():
    request = current_request()
    site_id = getattr(request, "site_id", None)
    if request and not site_id:
        site_id = request.session.get("site_id", None)
        if not site_id:
            domain = request.get_host().lower()
            if not site_id:
                try:
                    site = Site.objects.get(domain__iexact=domain)
                except Site.DoesNotExist:
                    pass
                else:
                    site_id = site.id
        if request and site_id:
            request.site_id = site_id
    if not site_id:
        site_id = os.environ.get("SITE_ID", settings.SITE_ID)

    return site_id


def populate_xheaders(request, response, model, object_id):
    """
    Adds the "X-Object-Type" and "X-Object-Id" headers to the given
    HttpResponse according to the given model and object_id -- but only if the
    given HttpRequest object has an IP address within the INTERNAL_IPS setting
    or if the request is from a logged in staff member.
    """
    from django.conf import settings

    if (request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS
        or (hasattr(request, 'user') and request.user.is_authenticated()
            and request.user.is_staff)):
        response['X-Object-Type'] = "%s.%s" % (model._meta.app_label, model._meta.object_name.lower())
        response['X-Object-Id'] = str(object_id)