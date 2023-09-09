from django.contrib import admin
from app_tours.models import *

# Register your models here.

class TourAdmin(admin.ModelAdmin):
    list_display = ['TourName','Status']
    search_fields = ['TourName']

class CountrysAdmin(admin.ModelAdmin):
    list_display = ['CountryName']
    search_fields = ['CountryName']

class LocationsAdmin(admin.ModelAdmin):
    list_display = ['City']
    search_fields = ['City']

class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['AccomName','TypeRoom']
    search_fields = ['AccomName']

admin.site.register(TourNames, TourAdmin)
admin.site.register(Countrys, CountrysAdmin)
admin.site.register(Locations, LocationsAdmin)
admin.site.register(Accommodation, AccommodationAdmin)