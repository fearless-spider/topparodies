import sitesngine.pages.admin
from sitesngine.pages.plugins.jsonexport.actions import export_pages_as_json
from sitesngine.pages.plugins.jsonexport.actions import import_pages_from_json
sitesngine.pages.admin.PageAdmin.add_action(export_pages_as_json)
sitesngine.pages.admin.PageAdmin.add_action(import_pages_from_json)