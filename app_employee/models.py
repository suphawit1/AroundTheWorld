from django.db import models

# Create your models here.

class Employees(models.Model):
    EmpID = models.IntegerField(max_length = 5, primary_key= True)
    EmpFirstName = models.CharField(max_length = 25)
    EmpLastName = models.CharField(max_length = 25)
    Job = models.CharField(max_length = 15)
    Contract = models.CharField(max_length = 10)
class GuideTour(models.Model):
    GuideTour = models.CharField(max_length = 25, primary_key = True)
    EmpID = models.ForeignKey(Employees,on_delete=models.CASCADE)
    Contact = models.CharField(max_length = 10)
    Status = models.TextField()
    