# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    published_on = models.DateTimeField()
    description = models.TextField()
    category = models.CharField(max_length=255, null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    page = models.URLField(null=True, blank=True)
    player = models.URLField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)

    counter = models.BigIntegerField(null=True, blank=True, default=0)
    rating = models.FloatField(null=True, blank=True, default=0.0)

    # show thumbnails
    thumb = models.URLField(null=True, blank=True)
    videoid = models.CharField(max_length=20, null=True, blank=True)
    public = models.BooleanField(default=True)

    def __repr__(self):
        return '<Video %s %s>' % (self.title, self.page)

    class Meta:
        ordering = ('-published_on',)
        get_latest_by = 'published_on'

    def __unicode__(self):
        return "%s" % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('video_detail', (), {
            'slug': self.slug,
            'pk': self.id
        })

    def save(self, *args, **kwargs):
        if self.published_on == None and self.public:
            self.published_on = datetime.now()
        if self.slug == None or self.slug == u'':
            self.slug = slugify(self.title)
        super(Video, self).save(*args, **kwargs)


class Twitter(models.Model):
    screen_name = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    avatar = models.URLField()
    tweet_id = models.CharField(max_length=55)

    def __repr__(self):
        return '<Twitter %s %s>' % (self.screen_name, self.tweet_id)
