# coding=utf-8

from contact.models import Feedback, CompanyInfo
from django.contrib import admin

class FedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'feedback_email', 'company')



admin.site.register(Feedback, FedbackAdmin)
admin.site.register(CompanyInfo)
