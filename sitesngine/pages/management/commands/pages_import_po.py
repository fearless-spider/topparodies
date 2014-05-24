from django.core.management.base import BaseCommand

from sitesngine.pages.utils import import_po_files


__author__ = 'fearless'  # "from birth till death"


class Command(BaseCommand):
    args = '<path>'
    help = import_po_files.__doc__

    def handle(self, *args, **options):
        import_po_files(*args)