from django.db import models

# Create your models here.

class Customer(models.Model):
    CusID = models.IntegerField(max_length = 5, primary_key= True)
    FirstName = models.CharField(max_length = 25)
    LastName = models.CharField(max_length = 25)
    Contract = models.CharField(max_length = 10)
    Email = models.EmailField(max_length = 25)
    BookID = models.ForeignKey('app_general.Booking',on_delete=models.CASCADE)