from django.shortcuts import render
from .forms import RegisterForm,UserEditForm
from django.contrib.auth import login,authenticate,logout
from django.http import HttpRequest,HttpResponseRedirect
from app_user.models import Customer
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_general.models import Booking,Payment
from django.contrib.auth.forms import AuthenticationForm
from datetime import timedelta
from django.utils import timezone

# Create your views here.

def register(request:HttpRequest):
    error_messages = ''
    if request.method == "POST":
        error_messages = ''
        form = RegisterForm(request.POST)

        error_user = form.errors.get('username')
        errors_pass = form.errors.get('password2')
        errors_contract = form.errors.get('Contract')
        errors_name = form.errors.get('FirstName')
        errors_lname = form.errors.get('LastName')
        errors_email = form.errors.get('Email')

        if errors_pass:
            error_messages += "***โปรดระบุรหัสผ่านให้ตรงกัน***\n"
        if  error_user:
            error_messages += "***ชื่อผู้ใช้นั้นได้ถูกใช้ไปแล้ว***\n"
        if  errors_name or errors_lname:
            error_messages += "***ชื่อและนามสกุลต้องเป็นตัวอักษรภาษาไทยเท่านั้น***\n"
        if  errors_contract:
            error_messages += "***เบอร์ติดต่อต้องเป็นตัวเลขเท่านั้น***\n"
        if  errors_email:
            error_messages += "***โปรดป้อนที่อยู่อีเมล์ให้ถูกต้อง***\n"
            
        if form.is_valid():
            user = form.save()
            error_messages = 'Pass'

            FirstNamedata = form.cleaned_data['FirstName']
            LastNamedata = form.cleaned_data['LastName']
            Contractdata = form.cleaned_data['Contract']
            Emaildata = form.cleaned_data['Email']

            Customer.objects.create(user=user, CusFirstName=FirstNamedata, CusLastName=LastNamedata, CusContract=Contractdata, CusEmail=Emaildata)

            login(request, user)
    else:
        form = RegisterForm()
    context = {"form":form,"error_mess":error_messages}
    return render(request, "app_user/register.html", context)

def loginview(request):
    error = 0
    if request.method == 'POST':
        error = 0
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            next_url = request.POST.get('next')
            if user is not None:
                login(request, user)
                if next_url:
                    return HttpResponseRedirect(next_url)
                return HttpResponseRedirect(reverse('home'))
        else:
            error = 1
    else:
        form = AuthenticationForm()
    context = {'form': form,'error':error}
    return render(request, "app_user/login.html", context)


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def dashboard_user(request):
    logged_in_user = request.user
    Cus = Customer.objects.get(user=logged_in_user)
    obj = Customer.objects.get(pk=Cus.CusID)
    checkedit = 0
    if request.method == "POST":
        form = UserEditForm(request.POST,instance=obj)
        print(form.errors)
        if form.is_valid():
            checkedit = 1
            form.save()
    else:
        initial_values = {
            'FirstName': Cus.CusFirstName,
            'LastName': Cus.CusLastName,
            'Contract': Cus.CusContract,
            'Email': Cus.CusEmail
        }
        form = UserEditForm(initial=initial_values,instance=obj)
    context = {"form":form,"check":checkedit}
    return render(request, "app_user/dashboard.html", context)

@login_required
def dashboard_book(request):
    logged_in_user = request.user
    Cus = Customer.objects.get(user=logged_in_user)
    
    bookedobj = Booking.objects.filter(cusID=Cus)
    
    one_day_threshold = timedelta(hours=17)
    
    current_datetime = timezone.now()
    for i in bookedobj:
        time_difference = current_datetime - i.BookTime
        if time_difference >= one_day_threshold and bookedobj[0].PayNumber.status == "รอการชำระ":
            i.PayNumber.status = "ยกเลิก"
            i.PayNumber.save()
            i.delete()
            continue
    logged_in_user = request.user
    Cus = Customer.objects.get(user=logged_in_user)
    
    try:
        booklist = Booking.objects.filter(cusID=Cus)
    except:
        booklist = None

    context = {"booklist":booklist}
    return render(request, "app_user/bookinglist.html", context)

@login_required
def dashboard_credit(request):
    check_credit = 0
    logged_in_user = request.user
    Cus = Customer.objects.get(user=logged_in_user)

    if request.method == "POST":
        add_Credit = request.POST.get('addCredit')
        Cus.Credits += int(add_Credit)
        check_credit = 1
        Cus.save()

    context = {'check':check_credit}

    return render(request, "app_user/credit.html", context)
