# coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns('about.views',
    #url(r'^portfolio/$', 'portfolio'),
    url(r'^about/$', 'about'),
)