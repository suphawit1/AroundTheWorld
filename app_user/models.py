from django.db import models

# Create your models here.

class Customer(models.Model):
    CusID = models.AutoField(primary_key= True)
    FirstName = models.CharField(max_length = 25)
    LastName = models.CharField(max_length = 25)
    Contract = models.CharField(max_length = 10)
    Email = models.EmailField(max_length = 25)
    def __str__(self) -> str:
        return '{} {}'.format(self.FirstName,self.LastName)