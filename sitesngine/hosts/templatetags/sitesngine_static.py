from django import template
from django.contrib.sites.models import Site
from django.templatetags.static import StaticNode
from django.contrib.staticfiles.storage import staticfiles_storage
from sitesngine.hosts.middleware import site_folder_name
from sitesngine.hosts.utils import current_site_id

__author__ = 'fearless' # "from birth till death"


register = template.Library()


class StaticFilesNode(StaticNode):

    def url(self, context):
        site_folder = site_folder_name(Site.objects.get(pk=current_site_id()))
        path = self.path.resolve(context)
        return staticfiles_storage.url(site_folder+'/'+path)


@register.tag('sitesngine_static')
def do_static(parser, token):
    """
    A template tag that returns the URL to a file
    using staticfiles' storage backend

    Usage::

        {% static path [as varname] %}

    Examples::

        {% static "myapp/css/base.css" %}
        {% static variable_with_path %}
        {% static "myapp/css/base.css" as admin_base_css %}
        {% static variable_with_path as varname %}

    """
    return StaticFilesNode.handle_token(parser, token)


def static(path):
    return staticfiles_storage.url(path)