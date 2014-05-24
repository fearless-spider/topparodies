from django.contrib.admin.widgets import AdminTextareaWidget, AdminTextInputWidget

__author__ = 'fearless' # "from birth till death"


class SubdomainTextarea(AdminTextareaWidget):
    """
    widget to render the Subdomain list
    """
    def render(self, name, value, attrs=None):
        if isinstance(value, list) or isinstance(value, tuple):
            value = u', '.join(value)
        return super(SubdomainTextarea, self).render(name, value, attrs)


class FolderNameInput(AdminTextInputWidget):
    class Media:
        js = ['js/sitesngine/admin.js']