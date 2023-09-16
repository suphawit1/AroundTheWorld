from django.contrib import admin
from app_general.models import *

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ['TourName']
    search_fields = ['TourName']

class PayAdmin(admin.ModelAdmin):
    list_display = ['cusID','status','Amount']
    search_fields = ['cusID']


admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PayAdmin)