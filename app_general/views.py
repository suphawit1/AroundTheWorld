from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_tours.models import Tours
from app_user.models import Customer
from .models import Payment,Booking
from .forms import BookingFrom,Fakecardform
from django.http import HttpRequest,HttpResponseRedirect
from app_user.models import Customer
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'app_general/home.html')

@login_required
def booking(request:HttpRequest, tour_name):
    logged_in_user = request.user
    Cus = Customer.objects.get(user=logged_in_user)
    one_tour = None
    try:
        one_tour = Tours.objects.get(TourName=tour_name)
    except:
        print("ไม่พบข้อมูล")
    
    if request.method == 'POST':
        form = BookingFrom(request.POST)
            
        seatData = request.POST.getlist('Seat')
        roomData = request.POST.getlist('Room')
        nameData = request.POST.getlist('Name')

        new_payment = Payment(cusID=Cus, Amount = one_tour.price*len(seatData))
        new_payment.save()
        for i in range (0,len(seatData)):
            Booking.objects.create(Seat=seatData[i],Room=roomData[i],TourName=one_tour,cusID=Cus,PayNumber = new_payment,FullName=nameData[i])

        return HttpResponseRedirect(reverse('payment', args=[new_payment.PayNumber]))
    else:
        form = BookingFrom(initial={'firstname': Cus.CusFirstName,'lastname': Cus.CusLastName,'TourName':one_tour.TourName})

    comboboxOptions = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'
                       ,'28','29','30','31','32','33','34','35','36','37','38','39','40']
    bookedobj = Booking.objects.filter(TourName=tour_name)
    bookedseatlist = []
    bookedroomlist = []
    for i in bookedobj:
        bookedseatlist.append(i.Seat)
        bookedroomlist.append(i.Room)

    AvcomboboxOptions = sorted(list(set(comboboxOptions) - set(bookedroomlist)))
    AvcomboboxOptions.sort()

    context = {'tour': one_tour,'form':form,'Cus':Cus,'room':AvcomboboxOptions,'bookedseatlist':bookedseatlist}
    return render(request,'app_general/booking.html', context)

def payment(request, pay_num):
    one_book = Booking.objects.get(PayNumber = pay_num)
    if request.method == 'POST':
        form = Fakecardform(request.POST)
        if form.is_valid():
            payment_update = Payment.objects.get(PayNumber = pay_num)
            payment_update.status = "completed"
            payment_update.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = Fakecardform()

    context = {'form':form,'book':one_book}
    return render(request,'app_general/payment.html',context)