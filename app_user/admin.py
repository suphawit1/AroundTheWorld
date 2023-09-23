from django.contrib import admin
from app_user.models import *

# Register your models here.


# Register your models here.

class cusAdmin(admin.ModelAdmin):
    list_display = ['CusID','CusFirstName','CusLastName','CusContract','CusEmail','Credits']
    search_fields = ['CusID','CusFirstName','CusLastName','CusEmail','CusContract']

admin.site.register(Customer, cusAdmin)