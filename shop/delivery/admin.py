from django.contrib import admin
from delivery.models import InfoColumn, FAQ


class InfoColumnAdmin(admin.ModelAdmin):
    list_display = ('column_text', 'header', 'state')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
# Register your models here.
admin.site.register(InfoColumn, InfoColumnAdmin)
admin.site.register(FAQ, FAQAdmin)