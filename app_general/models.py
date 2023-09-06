from django.db import models

# Create your models here.
class Booking(models.Model):
    BookID = models.IntegerField(max_length = 5,primary_key=True)
    Seat = models.TextField()
    Day = models.DateField()
    TourName = models.ForeignKey('app_tours.TourNames',on_delete=models.CASCADE)
    AccomName = models.ForeignKey('app_tours.Accommodation',on_delete=models.CASCADE)
    Room = models.TextField()
    AirlineName = models.IntegerField(max_length = 5)
    GuideName = models.ForeignKey('app_employee.GuideTour',on_delete=models.CASCADE)
