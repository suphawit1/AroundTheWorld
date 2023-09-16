from django.db import models

# Create your models here.

class Countrys(models.Model):
    CountryID = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length = 15)
    Region = models.CharField(max_length = 10, null=True)

    def __str__(self) -> str:
        return '{} (id = {})'.format(self.CountryName,self.CountryID)
    
class Locations(models.Model):
    LocationName = models.CharField(max_length = 25,primary_key=True)
    CountryID = models.ForeignKey(Countrys,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}'.format(self.LocationName)

class Accommodation(models.Model):
    AccomName = models.CharField(max_length = 25, primary_key= True)
    TypeRoom = models.TextField()
    CountryID = models.ForeignKey(Countrys,on_delete=models.CASCADE)
    LocationName = models.ForeignKey(Locations,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{}'.format(self.AccomName)
    
class TourNames(models.Model):
    STATUS = [
        ("open","Open"),
        ("close","Close"),
        ("full","Full")
    ]
    TourName = models.CharField(max_length = 25, primary_key= True)
    Status = models.TextField(choices=STATUS,default='open')
    TripDuration = models.TextField()
    LocationName = models.ForeignKey(Locations,on_delete=models.CASCADE)
    Accommodation = models.ForeignKey(Accommodation,on_delete=models.CASCADE)
    GuideName = models.ForeignKey('app_employee.GuideTour',on_delete=models.CASCADE)
    AirlineName = models.CharField(max_length = 25)
    Day = models.DateField()
    price = models.FloatField(default=0)
    def __str__(self) -> str:
        return '{}'.format(self.TourName)

    