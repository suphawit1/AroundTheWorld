from django.db import models

# Create your models here.

class Countrys(models.Model):
    CountryID = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length = 15)
    
    def __str__(self) -> str:
        return '{} (id = {})'.format(self.CountryName,self.CountryID)
    
class Locations(models.Model):
    LocationID = models.AutoField(primary_key=True)
    City = models.CharField(max_length = 25)
    CountryID = models.ForeignKey(Countrys,on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return '{} (id = {})'.format(self.City,self.LocationID)
    
class Accommodation(models.Model):
    AccomName = models.CharField(max_length = 25, primary_key= True)
    City = models.CharField(max_length= 25)
    TypeRoom = models.TextField()
    CountryID = models.ForeignKey(Countrys,on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return '{}'.format(self.AccomName)
    
class TourNames(models.Model):
    TourName = models.CharField(max_length = 25, primary_key= True)
    Status = models.TextField()
    TripDuration = models.TextField()
    LocationID = models.ForeignKey(Locations,on_delete=models.SET_NULL, null=True)
    CountryID = models.ForeignKey(Countrys,on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return '{}'.format(self.TourName)

    