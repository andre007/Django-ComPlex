# coding=utf-8

from django.conf.urls import patterns, url, include

urlpatterns = patterns('product.views',
    #url(r'^portfolio/$', 'portfolio'),
    url(r'^product_list/(?P<id>\d+)/$', 'product_list'),
    url(r'^product_detail/(?P<id>\d+)/$', 'product_detail'),
)
