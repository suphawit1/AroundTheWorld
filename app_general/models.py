from django.db import models

# Create your models here.
class Payment(models.Model):
    STATUS = [
        ("รอการชำระ","รอการชำระ"),
        ("สำเร็จ","สำเร็จ"),
        ("ยกเลิก","ยกเลิก")
    ]
    PayNumber = models.AutoField(primary_key=True)
    cusID = models.ForeignKey('app_user.Customer',on_delete=models.CASCADE)
    status = models.TextField(choices=STATUS, default="รอการชำระ")
    Amount = models.FloatField()

class Booking(models.Model):
    BookID = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length= 50)
    Seat = models.TextField()
    Room = models.TextField()
    TourName = models.ForeignKey('app_tours.Tours',on_delete=models.CASCADE)
    BookTime = models.DateTimeField(auto_now_add=True)
    cusID = models.ForeignKey('app_user.Customer',on_delete=models.CASCADE)
    PayNumber = models.ForeignKey(Payment,on_delete=models.CASCADE)

