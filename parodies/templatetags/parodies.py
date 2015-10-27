from django import template
from django.template.loader import render_to_string
from ..models import Twitter

__author__ = 'fearless'

register = template.Library()

@register.tag('get_twitter')
def get_models(parser,token):
    return GetTwitter()

class GetTwitter(template.Node):
    def render(self, context):
        context['twitter'] = Twitter.objects.order_by('-created_at').all()[:50]
        return render_to_string('parodies/twitter/twitter_list.html', context)

@register.inclusion_tag('parodies/video/render_video.html')
def render_video(video_instance, width=320, height=240):
    """
    This is a intelligent inclusion tag that will try do determine what kind
    of video ``video_instance`` is, and then render the correct HTML for this
    video.

    ``width`` and ``height`` refers to the width and height of the video.

    Example Usage:
        {% render_video video 640 480 %}

    """
    try:
        if video_instance.video:
            video_type = 'video'
    except:
        pass

    return locals()