from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    CusID = models.AutoField(primary_key= True)
    CusFirstName = models.CharField(max_length = 25)
    CusLastName = models.CharField(max_length = 25)
    CusContract = models.CharField(max_length = 10)
    CusEmail = models.EmailField(max_length = 25,unique=True)
    Credits = models.FloatField(default=99999999)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{} {}'.format(self.CusFirstName,self.CusLastName)