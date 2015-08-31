# coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns('delivery.views',
    #url(r'^portfolio/$', 'portfolio'),
    url(r'^delivery/$', 'delivery'),
)