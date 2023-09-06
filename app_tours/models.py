from django.db import models

# Create your models here.

class Countrys(models.Model):
    CountryID = models.IntegerField(max_length = 5, primary_key= True)
    CountryName = models.CharField(max_length = 15)
class Locations(models.Model):
    LocationID = models.IntegerField(max_length = 5,primary_key= True)
    City = models.CharField(max_length = 25)
    CountryID = models.ForeignKey(Countrys,on_delete=models.CASCADE)
class Accommodation(models.Model):
    AccomName = models.CharField(max_length = 25, primary_key= True)
    City = models.CharField(max_length= 25)
    TypeRoom = models.TextField()
    CountryID = models.ForeignKey(Countrys,on_delete=models.CASCADE)
class TourNames(models.Model):
    TourName = models.CharField(max_length = 25, primary_key= True)
    Status = models.TextField()
    TripDuration = models.TextField()
    LocationID = models.ForeignKey(Locations,on_delete=models.CASCADE)
    CountryID = models.ForeignKey(Countrys,on_delete=models.CASCADE)