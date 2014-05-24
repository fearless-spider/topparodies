from django.contrib import admin
from django.contrib.auth.models import User
from sitesngine.hosts.models import SitePermission

__author__ = 'fearless' # "from birth till death"


class SitePermissionInline(admin.TabularInline):
    model = SitePermission
    max_num = 1
    can_delete = False


class SitePermissionUserAdmin(admin.ModelAdmin):
    inlines = [SitePermissionInline,]

admin.site.unregister(User)
admin.site.register(User, SitePermissionUserAdmin)
