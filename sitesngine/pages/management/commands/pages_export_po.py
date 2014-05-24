from django.core.management.base import BaseCommand

from sitesngine.pages.utils import export_po_files


__author__ = 'fearless'  # "from birth till death"


class Command(BaseCommand):
    args = '<path>'
    help = export_po_files.__doc__

    def handle(self, *args, **options):
        export_po_files(*args)