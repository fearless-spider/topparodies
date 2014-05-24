from django.db import models
from django.db.models.signals import post_save
from sitesngine.hosts.managers import CurrentSiteManager
from sitesngine.hosts.utils import current_site_id
from django.utils.translation import ugettext_lazy as _

__author__ = 'fearless' # "from birth till death"


class SiteRelated(models.Model):
    objects = CurrentSiteManager()

    class Meta:
        abstract = True

    site = models.ForeignKey("sites.Site", editable=False)

    def save(self, update_site=False, *args, **kwargs):
        """
        Set the site to the current site when the record is first
        created, or the ``update_site`` argument is explicitly set
        to ``True``.
        """
        if update_site or not self.id:
            self.site_id = current_site_id()
        super(SiteRelated, self).save(*args, **kwargs)


class SitePermission(models.Model):
    """
    Permission relationship between a user and a site that's
    used instead of ``User.is_staff``, for admin and inline-editing
    access.
    """

    user = models.ForeignKey('auth.User', verbose_name=_("Author"),
        related_name="%(class)ss")
    sites = models.ManyToManyField("sites.Site", blank=True,
                                   verbose_name=_("Sites"))

    class Meta:
        verbose_name = _("Site permission")
        verbose_name_plural = _("Site permissions")


def create_site_permission(sender, **kw):
    sender_name = "%s.%s" % (sender._meta.app_label, sender._meta.object_name)
    if sender_name.lower() != 'auth.user':
        return
    user = kw["instance"]
    if user.is_staff and not user.is_superuser:
        perm, created = SitePermission.objects.get_or_create(user=user)
        if created or perm.sites.count() < 1:
            perm.sites.add(current_site_id())

# We don't specify the user model here, because with 1.5's custom
# user models, everything explodes. So we check the name of it in
# the signal.
post_save.connect(create_site_permission)
