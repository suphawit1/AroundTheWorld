from django.contrib import admin

from app_employee.models import *

# Register your models here.

class empAdmin(admin.ModelAdmin):
    list_display = ['EmpFirstName','EmpLastName']
    search_fields = ['EmpFirstName']

class guideAdmin(admin.ModelAdmin):
    list_display = ['GuideName','Status']
    search_fields = ['GuideName']


admin.site.register(Employees, empAdmin)
admin.site.register(GuideTour, guideAdmin)