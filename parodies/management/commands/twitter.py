# -*- coding: utf-8 -*-
from datetime import datetime
import time
from django.core.management.base import NoArgsCommand
from parodies.models import Twitter
from twython import Twython

__author__ = 'bespider'

APP_KEY = 'p7duD7524hXwGidK927Iw'
APP_SECRET = '6S0pna9aRNEcyNLk5Syu9iVzlIXMMzDQCCFs7LF6g'
OAUTH_TOKEN = '80306678-kOGQka8ukwUD8PyeRTH6rd2CUVZidMdnvvKDAWFI'
OAUTH_TOKEN_SECRET = 'gRKPt2FEQnwMtbFRYIcKk4In11E8zFd7fvR3HwdHbb4'


class TagCrawler(object):
    def __init__(self, tag):
        self.tag = tag

    def search(self):
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        return twitter.search_gen(self.tag)

    def get_twitter_date(self, date_str):
        time_struct = time.strptime(date_str, "%a %b %d %H:%M:%S +0000 %Y")
        return datetime.fromtimestamp(time.mktime(time_struct))


class Command(NoArgsCommand):
    help = 'Help text goes here'

    def handle(self, **options):
        print "This is a command"

        tagCrawler = TagCrawler(tag="#parody")
        tweets = tagCrawler.search()
        for tweet in tweets:
            Twitter.objects.get_or_create(
                tweet_id=tweet['id_str'],
                defaults={
                    'screen_name': tweet['user']['screen_name'].encode("latin-1", "ignore").decode("latin-1", "ignore"),
                    'content': tweet['text'].encode("latin-1", "ignore").decode("latin-1", "ignore"),
                    'created_at': tagCrawler.get_twitter_date(tweet['created_at']),
                    'avatar': tweet['user']['profile_image_url'],
                    'tweet_id': tweet['id_str']
                }
            )
