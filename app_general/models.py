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
    Amount = models.FloatField()

class Booking(models.Model):
    BookID = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length= 50)
    Seat = models.TextField()
    TourName = models.ForeignKey('app_tours.TourNames',on_delete=models.CASCADE)
    Room = models.TextField()
    cusID = models.ForeignKey('app_user.Customer',on_delete=models.CASCADE)
    payNum = models.ForeignKey(Payment,on_delete=models.CASCADE)


