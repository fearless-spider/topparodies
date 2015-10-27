# -*- coding: utf-8 -*-
from optparse import make_option
import urlparse
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
import gdata.youtube
import gdata.youtube.service
from parodies.models import Video

__author__ = 'bespider'

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--index', '-i', dest='index',
            help='Index of youtube video > 0'),
        make_option('--time', '-t', dest='time',
            help='Time of youtube video(today,this_week,this_month,all_time)'),
        )
    help = 'Search parodies on youtube'

    def handle(self, **options):
        print "Start search parodies for " + options.get('time')

        time = options.get('time')
        index = options.get('index')

        yt_service = gdata.youtube.service.YouTubeService()
        query = gdata.youtube.service.YouTubeVideoQuery()

        query.vq = "parody"
        query.orderby = "relevance"
        query.racy = "include"
        query.start_index = index
        query.max_results = 50

        if time:
            query.time = time

        feed = yt_service.YouTubeQuery(query)

        for entry in feed.entry:
            parsed_url = urlparse.urlparse(entry.id.text)

            title = "%s" % entry.media.title.text
            slug = slugify(title)
            published_on = entry.published.text

            counter = 1

            if hasattr(entry.statistics, 'view_count'):
                counter = entry.statistics.view_count

            rating = 1

            if hasattr(entry.rating,'average'):
                rating=entry.rating.average

            if entry.media.description.text:
                description = entry.media.description.text
            else:
                description = ''

            category = "%s" % entry.media.category[0].text
            tags = "%s" % entry.media.keywords.text
            page = entry.media.player.url
            player = entry.GetSwfUrl()
            duration = entry.media.duration.seconds
            thumb = entry.media.thumbnail[0].url

            videoid = parsed_url.path.split('/')[3]

            video, created = Video.objects.get_or_create(
                videoid = videoid,
                defaults={
                    'title':title,
                    'slug':slug,
                    'published_on':published_on,
                    'counter':counter,
                    'rating':rating,
                    'description':description,
                    'category':category,
                    'tags':tags,
                    'page':page,
                    'player':player,
                    'duration':duration,
                    'thumb':thumb,
                    'videoid':videoid,
                }
            )
            if not created:
                video.rating = rating
                video.counter = counter
                video.save()
