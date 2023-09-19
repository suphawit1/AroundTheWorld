from django.contrib import admin
from app_user.models import *

# Register your models here.


# Register your models here.

class cusAdmin(admin.ModelAdmin):
    list_display = ['CusFirstName','CusLastName']
    search_fields = ['CusFirstName']

admin.site.register(Customer, cusAdmin)