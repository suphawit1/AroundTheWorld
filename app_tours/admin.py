from django.contrib import admin
from app_tours.models import *

# Register your models here.

class TourAdmin(admin.ModelAdmin):
    list_display = ['TourName','TripDuration','Status','Day','price']
    search_fields = ['TourName','Day','TripDuration']
    list_filter = ['Status']

class CountrysAdmin(admin.ModelAdmin):
    list_display = ['CountryName','Region']
    search_fields = ['CountryName','Region']

class LocationsAdmin(admin.ModelAdmin):
    list_display = ['LocationName','CountryName']
    search_fields = ['LocationName']
    list_filter = ['CountryName__CountryName']

class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['AccomName','TypeRoom','CountryName','LocationName']
    search_fields = ['AccomName']
    list_filter = ['TypeRoom','CountryName__CountryName']
class Tourlocation(admin.ModelAdmin):
    filter_horizontal = ('ListLoID',)

class CombinedTourAdmin(Tourlocation, TourAdmin):
    pass



admin.site.register(Tours, CombinedTourAdmin)
admin.site.register(Countrys, CountrysAdmin)
admin.site.register(Locations, LocationsAdmin)
admin.site.register(Accommodation, AccommodationAdmin)