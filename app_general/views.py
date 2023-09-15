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
            dayData = form.cleaned_data['Day']
            roomData = form.cleaned_data['Room']
            airData = form.cleaned_data['AirlineName']
            AccomNameData = form.cleaned_data['AccomName']
            GuideNameData = form.cleaned_data['GuideName']
            TourNamesData = one_tour
            cusIDData = Cus
            request.session['type'] = form.cleaned_data['paymenttype']


            new_payment = Payment(cusID=Cus, Amount= 1000)
            new_payment.save()

            Booking.objects.create(Seat=seatData,Day=dayData,Room=roomData,AirlineName=airData,AccomName=AccomNameData,
                                   GuideName=GuideNameData,TourName=TourNamesData,cusID=cusIDData,payNum = new_payment)

            
            new_payment = Payment(cusID=Cus, Amount= 1000)
            new_payment.save()
            
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

    type = request.session.get('type')
    context = {'type': type,'form':form}
    return render(request,'app_general/payment.html',context)