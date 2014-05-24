from django.conf.urls import patterns, url
from django.contrib.admin.views.decorators import staff_member_required
from views import ElfinderConnectorView
from sitesngine.elfinder.views_tinymce import tinymce_filebrowser_script_view, tinymce_filebrowser_dialog_view

urlpatterns = patterns('',
                       url(r'^yawd-connector/(?P<optionset>.+)/(?P<start_path>.+)/$',
                           staff_member_required(ElfinderConnectorView.as_view()),
                           name='yawdElfinderConnectorView'),
                       url(r'^tinymce/filebrowser-script/$', tinymce_filebrowser_script_view,
                           name='elfinder_tinymce_filebrowser_script'),
                       url(r'^tinymce/filebrowser-dialog/$', tinymce_filebrowser_dialog_view,
                           name='elfinder_tinymce_filebrowser_dialog'),
)