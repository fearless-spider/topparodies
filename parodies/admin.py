from django.contrib import admin
from parodies.models import Twitter, Video

__author__ = 'fearless'

def publish_videos(modeladmin, request, queryset):
    """ Mark selected videos as public """
    queryset.update(public=True)
    # Quickly call the save() method for every video so that the dates are updated
    for video in queryset:
        video.save()
publish_videos.short_description = "Publish selected videos"

def unpublish_videos(modeladmin, request, queryset):
    """ Unmark selected videos as public """
    queryset.update(public=False)
unpublish_videos.short_description = "Unpublish selected Videos"


class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_on'
    list_display = ['title', 'slug', 'published_on', 'public',]
    list_filter = ['published_on','public']
    search_fields = ['title', 'description', 'tags']
    fieldsets = (
        ('Video Details', {'fields': [
            'title', 'slug', 'description', 'tags', 'category', 'public',
            'published_on',
            ]}),
        )
    actions = [publish_videos, unpublish_videos]


admin.site.register(Video, VideoAdmin)
admin.site.register(Twitter)
