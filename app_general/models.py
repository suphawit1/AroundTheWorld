from django.db import models

# Create your models here.
class Payment(models.Model):
    STATUS = [
        ("pending","Pending"),
        ("completed","Completed"),
        ("canceled","Canceled")
    ]
    PayNumber = models.AutoField(primary_key=True)
    cusID = models.ForeignKey('app_user.Customer',on_delete=models.CASCADE)
    status = models.TextField(choices=STATUS, default="pending")
    Amount = models.IntegerField()

class Booking(models.Model):
    BookID = models.AutoField(primary_key=True)
    Seat = models.TextField()
    Day = models.DateField()
    TourName = models.ForeignKey('app_tours.TourNames',on_delete=models.CASCADE)
    AccomName = models.ForeignKey('app_tours.Accommodation',on_delete=models.CASCADE)
    Room = models.TextField()
    AirlineName = models.CharField(max_length = 25)
    GuideName = models.ForeignKey('app_employee.GuideTour',on_delete=models.CASCADE)
    cusID = models.ForeignKey('app_user.Customer',on_delete=models.CASCADE)
    payNum = models.ForeignKey(Payment,on_delete=models.SET_NULL, null=True)


