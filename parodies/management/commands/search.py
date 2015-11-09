# -*- coding: utf-8 -*-
from optparse import make_option
import urlparse
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from parodies.models import Video

__author__ = 'bespider'


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDBYrj89EB0UEVIvVgpPqnB5t2CNdaygxQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--index', '-i', dest='index',
            help='Index of youtube video > 0'),
        make_option('--time', '-t', dest='time',
            help='Time of youtube video(today,this_week,this_month,all_time)'),
        )
    help = 'Search parodies on youtube'

    def handle(self, **options):
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)

        # Call the search.list method to retrieve results matching the specified
        # query term.
        search_response = youtube.search().list(
            q="parody",
            part="id,snippet",
            maxResults=50
        ).execute()

        videos = []
        channels = []
        playlists = []

        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        for search_result in search_response.get("items", []):
            id = search_result['id']
            videoId = id.get('videoId', None)
            if videoId:
                title = search_result['snippet']['title']
                slug = slugify(title)
                published_on = search_result['snippet']['publishedAt']
                description = search_result['snippet']['description']
                thumb = search_result['snippet']['thumbnails']['high']['url']
                parsed_url = "https://www.youtube.com/watch?v="+id.get('videoId')
                counter = 1
                rating = 1

                video, created = Video.objects.get_or_create(
                    videoid = videoId,
                    defaults={
                        'title':title,
                        'slug':slug,
                        'published_on':published_on,
                        'counter':counter,
                        'rating':rating,
                        'description':description,
                        'category':"",
                        'tags':"",
                        'page':"",
                        'player':parsed_url,
                        'duration':0,
                        'thumb':thumb,
                        'videoid':videoId,
                    }
                )
                if not created:
                    video.rating = rating
                    video.counter = counter
                    video.save()
