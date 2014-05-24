# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType
from django.views.generic import TemplateView, ListView, DetailView
from parodies.models import Video


class IndexView(TemplateView):
    template_name = 'parodies/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest'] = Video.objects.filter(public=True).exclude(slug='').order_by('-published_on')[:16]
        context['top'] = Video.objects.filter(public=True).exclude(slug='').order_by('-counter')[:16]

        return context


class PrivacyView(TemplateView):
    template_name = 'parodies/privacy.html'


class TermsView(TemplateView):
    template_name = 'parodies/terms.html'


class VideoDetail(DetailView):
    template_name = 'parodies/video/video_detail.html'
    model = Video


class TopVideoListView(ListView):
    template_name = 'parodies/video/video_list.html'
    model = Video
    paginate_by = 25

    def get_queryset(self):
        return Video.objects.filter(public=True).exclude(slug='').order_by('-counter')

    def get_context_data(self, **kwargs):
        context = super(TopVideoListView, self).get_context_data(**kwargs)
        context['title'] = 'Top'
        return context


class LatestVideoListView(ListView):
    template_name = 'parodies/video/video_list.html'
    model = Video
    paginate_by = 25

    def get_queryset(self):
        return Video.objects.filter(public=True).exclude(slug='').order_by('-published_on')

    def get_context_data(self, **kwargs):
        context = super(LatestVideoListView, self).get_context_data(**kwargs)
        context['title'] = 'Latest'
        return context


class TodayVideoListView(ListView):
    template_name = 'parodies/video/video_todaylist.html'
    model = Video
    paginate_by = 25

    def get_queryset(self):
        return Video.objects.filter(public=True, published_on__day=(datetime.today()).day).exclude(slug='').order_by('-published_on')


class ThisWeekVideoListView(ListView):
    template_name = 'parodies/video/video_this_weeklist.html'
    model = Video
    paginate_by = 25

    def get_queryset(self):
        return Video.objects.filter(public=True, published_on__gte=(datetime.today() - timedelta(days=7))).exclude(slug='').order_by(
            '-published_on')


class ThisMonthVideoListView(ListView):
    template_name = 'parodies/video/video_this_monthlist.html'
    model = Video
    paginate_by = 25

    def get_queryset(self):
        return Video.objects.filter(public=True, published_on__month=(datetime.today().month)).exclude(slug='').order_by(
            '-published_on')


class GroupVideoListView(ListView):
    template_name = 'parodies/video/video_group.html'
    model = Video
    paginate_by = 25

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Video.objects.filter(public=True, title__icontains=slug).order_by('-published_on')

    def get_context_data(self, **kwargs):
        context = super(GroupVideoListView, self).get_context_data(**kwargs)

        slug = self.kwargs['slug']
        titles = {
            'bieber': "Justin Bieber Parodies",
            'rihanna': "Rihanna Parodies",
            'iphone': "Apple iPhone Parodies",
            'google': "Google Parodies",
            'samsung': "Samsung Parodies",
            'duty': "Call Of Duty Parodies",
            'minecraft': "Minecraft Parodies",
            'lost': "LOST TV Series Parodies",
            '300': "300 The Movie Parodies",
            'minaj': "Nicki Minaj Parodies",
            'direction': "One Direction Parodies",
            'gangnam': "Gangnam Style Parodies",
            'miserables': "Les Miserables Parodies",
            'wars': "Star Wars Parodies",
            'daft': "Daft Punk Parodies",
            'avengers': "The Avengers Parodies",
            'superman': "Superman Parodies",
            'ipad': "Apple iPad Parodies",
            'windows': "Windows Parodies",
            'gta': "Grand Theft Auto (GTA) Parodies",
            'halo': "HALO Parodies",
            'spiderman': "Spiderman Parodies",
            'beyonce': "Beyonce Parodies",
            'gaga': "Lady Gaga Parodies",
            'obama': "Barack Obama Parodies",
            'porn': "Porn Parodies",
        }
        context['title'] = titles.get(slug)
        return context
