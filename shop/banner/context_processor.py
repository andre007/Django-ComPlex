# coding=utf-8

from banner.models import Banner


def contex_banner(request):
    banners = Banner.objects.filter(state=1)
    return {'banner_title': banners}
