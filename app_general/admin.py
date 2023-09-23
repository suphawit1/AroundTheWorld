from django.contrib import admin
from app_general.models import *

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ['BookID','TourName','FullName','Seat','Room','BookTime']
    search_fields = ['TourName__TourName','FullName']
    list_filter = ['TourName__TourName']

class PayAdmin(admin.ModelAdmin):
    list_display = ['cusID','status','Amount']
    search_fields = ['cusID','Amount']
    list_filter = ['status']


admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PayAdmin)