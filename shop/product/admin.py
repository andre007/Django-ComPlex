# coding=utf-8

from product.models import Product, Categories, Photo, Miniphoto
from django.contrib import admin
#from django_summernote.admin import SummernoteModelAdmin


#class ProductAdmin(SummernoteModelAdmin):
 #   list_display = ('name', 'short_text', 'date_creation', 'category')
  #  filter_horizontal = ('photos', 'drawing', 'files')


admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Photo)
admin.site.register(Miniphoto)

