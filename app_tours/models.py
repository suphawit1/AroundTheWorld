from django.db import models

# Create your models here.

class Countrys(models.Model):
    CountryName = models.CharField(primary_key=True, max_length = 25)
    Region = models.CharField(max_length = 10)

    def __str__(self) -> str:
        return '{}'.format(self.CountryName)
    
class Locations(models.Model):
    LocationName = models.CharField(max_length = 50,primary_key=True)
    CountryName = models.ForeignKey(Countrys,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}'.format(self.LocationName)

class Accommodation(models.Model):
    AccomName = models.CharField(max_length = 25, primary_key= True)
    TypeRoom = models.TextField()
    CountryName = models.ForeignKey(Countrys,on_delete=models.CASCADE)
    LocationName = models.ForeignKey(Locations,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{}'.format(self.AccomName)

class Tours(models.Model):
    STATUS = [
        ("เปิด","เปิด"),
        ("ปิด","ปิด"),
        ("เต็ม","เต็ม")
    ]
    TourName = models.CharField(primary_key= True,max_length = 25)
    Status = models.TextField(choices=STATUS,default='open')
    TripDuration = models.TextField()
    Accommodation = models.ForeignKey(Accommodation,on_delete=models.CASCADE)
    CountryName =models.ForeignKey(Countrys,on_delete=models.CASCADE)
    GuideName = models.ForeignKey('app_employee.GuideTour',on_delete=models.CASCADE)
    ListLoID = models.ManyToManyField(Locations)
    Day = models.DateField()
    price = models.FloatField(default=0)
    FlightNo = models.IntegerField()
    Detail = models.TextField(null=True, blank= True)
    immage = models.CharField(max_length = 50, null=True, blank= True)
    def __str__(self) -> str:
        return '{}'.format(self.TourName)

