from django.db import models

# Create your models here.

class Employees(models.Model):
    EmpID = models.AutoField(primary_key= True)
    EmpFirstName = models.CharField(max_length = 25)
    EmpLastName = models.CharField(max_length = 25)
    Job = models.CharField(max_length = 15)
    Contract = models.CharField(max_length = 10)
    def __str__(self) -> str:
        return '{} {}'.format(self.EmpFirstName,self.EmpLastName)
class GuideTour(models.Model):
    STATUS = [
        ("available","Available"),
        ("not_available","Not Available")
    ]
    GuideName = models.CharField(max_length = 25, primary_key = True)
    EmpID = models.ForeignKey(Employees,on_delete=models.CASCADE)
    Contact = models.CharField(max_length = 10)
    Status = models.TextField(choices=STATUS, default="available")
    def __str__(self) -> str:
        return '{}'.format(self.GuideName)
    