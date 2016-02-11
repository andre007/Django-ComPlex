from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('banner.urls')),
    url(r'^', include('product.urls')),
    #url(r'^search/', include('haystack.urls')),
    url(r'^', include('profile.urls')),
    url(r'^', include('booking.urls')),
    url(r'^', include('contact.urls')),
    url(r'^', include('about.urls')),
    url(r'^', include('delivery.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
