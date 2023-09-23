from django.contrib import admin

from app_employee.models import *

# Register your models here.

class empAdmin(admin.ModelAdmin):
    list_display = ['EmpID','EmpFirstName','EmpLastName','Job','EmpContract',"EmpEmail"]
    search_fields = ['EmpFirstName','EmpLastName','Job','EmpContract']
    list_filter = ['Job']

class guideAdmin(admin.ModelAdmin):
    list_display = ['GuideName','GuideContact','Status','EmpID']
    search_fields = ['GuideName','GuideContact']
    list_filter = ['Status']


admin.site.register(Employees, empAdmin)
admin.site.register(GuideTour, guideAdmin)