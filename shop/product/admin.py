# coding=utf-8

from product.models import Product, Categories, Photo, Miniphoto
from django.contrib import admin
#from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_text', 'price', 'category', 'state')


admin.site.register(Product, ProductAdmin)
admin.site.register(Categories)
admin.site.register(Photo)
admin.site.register(Miniphoto)

