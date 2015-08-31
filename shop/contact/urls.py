# coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns('contact.views',
    #url(r'^portfolio/$', 'portfolio'),
    url(r'^contact/$', 'contact'),
    url(r'^feedback_thanx/$', 'thanx'),
)