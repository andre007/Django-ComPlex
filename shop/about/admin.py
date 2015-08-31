from django.contrib import admin
from about.models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_text', 'state')
# Register your models here.
admin.site.register(About, AboutAdmin)