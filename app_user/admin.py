from django.contrib import admin
from app_user.models import *

# Register your models here.


# Register your models here.

class cusAdmin(admin.ModelAdmin):
    list_display = ['FirstName','LastName']
    search_fields = ['FirstName']

admin.site.register(Customer, cusAdmin)