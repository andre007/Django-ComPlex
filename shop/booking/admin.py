from django.contrib import admin
from booking.models import Booking, Mail

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_sum', 'user_name', 'user_sec_name', 'user_mail')
# Register your models here.
admin.site.register(Booking, BookingAdmin)
admin.site.register(Mail)