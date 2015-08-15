# coding=utf-8

from banner.models import Banner
from django.contrib import admin


class BannerAdmin(admin.ModelAdmin):
    list_display = ('string_one', 'string_two', 'string_three','state')


admin.site.register(Banner, BannerAdmin)
