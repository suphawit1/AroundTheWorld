from django.shortcuts import render
from .forms import RegisterForm,UserEditForm
from django.contrib.auth import login
from django.http import HttpRequest,HttpResponseRedirect
from app_user.models import Customer
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_general.models import Booking

# Create your views here.

def register(request:HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        print(form.errors)
        if form.is_valid():
            user = form.save()

            FirstNamedata = form.cleaned_data['FirstName']
            LastNamedata = form.cleaned_data['LastName']
            Contractdata = form.cleaned_data['Contract']
            Emaildata = form.cleaned_data['Email']

            Customer.objects.create(user=user, CusFirstName=FirstNamedata, CusLastName=LastNamedata, CusContract=Contractdata, CusEmail=Emaildata)

            login(request, user)

            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()

    context = {"form":form}
    return render(request, "app_user/register.html", context)

@login_required
def dashboard_user(request):
    logged_in_user = request.user
    Cus = Customer.objects.get(user=logged_in_user)
    obj = Customer.objects.get(pk=Cus.CusID)
    if request.method == "POST":
        form = UserEditForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        initial_values = {
            'FirstName': Cus.CusFirstName,
            'LastName': Cus.CusLastName,
            'Contract': Cus.CusContract,
            'Email': Cus.CusEmail
        }
        form = UserEditForm(initial=initial_values,instance=obj)
    context = {"form":form}
    return render(request, "app_user/dashboard.html", context)

@login_required
def dashboard_book(request):
    logged_in_user = request.user
    Cus = Customer.objects.get(user=logged_in_user)

    try:
        booklist = Booking.objects.filter(cusID=Cus)
    except:
        booklist = None

    context = {"booklist":booklist}
    return render(request, "app_user/bookinglist.html", context)