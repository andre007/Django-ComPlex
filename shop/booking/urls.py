from django.conf.urls import patterns, url, include

urlpatterns = patterns('booking.views',
    #url(r'^portfolio/$', 'portfolio'),
    #COSTYL DOWN HERE
    url(r'^booking/$', 'booking'),
    url(r'^registered_booking/$', 'registered_booking'),
    url(r'^thanx/$', 'thanx'),
    #url(r'^cart/$', 'get_cart'),
    
)
