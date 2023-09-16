from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_tours.models import TourNames
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
        one_tour = TourNames.objects.get(TourName=tour_name)
    except:
        print("ไม่พบข้อมูล")
    
    if request.method == 'POST':
        form = BookingFrom(request.POST)

        if form.is_valid():
            
            seatData = form.cleaned_data['Seat']
            roomData = form.cleaned_data['Room']
            TourNamesData = one_tour
            cusIDData = Cus


            new_payment = Payment(cusID=Cus, Amount = one_tour.price)
            new_payment.save()

            Booking.objects.create(Seat=seatData,Room=roomData,TourName=TourNamesData,cusID=cusIDData,payNum = new_payment)

            
            return HttpResponseRedirect(reverse('payment', args=[new_payment.PayNumber]))
    else:
        form = BookingFrom(initial={'firstname': Cus.FirstName,'lastname': Cus.LastName,'TourName':one_tour.TourName})

    context = {'tour': one_tour,'form':form,'Cus':Cus}
    return render(request,'app_general/booking.html', context)

def payment(request, pay_num):
    if request.method == 'POST':
        form = Fakecardform(request.POST)
        if form.is_valid():
            payment_update = Payment.objects.get(PayNumber = pay_num)
            payment_update.status = "completed"
            payment_update.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = Fakecardform()

    context = {'form':form}
    return render(request,'app_general/payment.html',context)