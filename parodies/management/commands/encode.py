# -*- coding: utf-8 -*-

__author__ = 'fearless'

from django.core.management.base import NoArgsCommand

from ...utils.encode import encode_video_set


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        """ Encode all pending streams """
        encode_video_set()