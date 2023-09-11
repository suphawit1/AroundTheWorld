from django.shortcuts import render
from app_user.forms import RegisterForm
from django.contrib.auth import login
from django.http import HttpRequest,HttpResponseRedirect
from app_user.models import Customer
from django.urls import reverse

# Create your views here.

def register(request:HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            FirstNamedata = form.cleaned_data['FirstName']
            LastNamedata = form.cleaned_data['LastName']
            Contractdata = form.cleaned_data['Contract']
            Emaildata = form.cleaned_data['Email']

            Customer.objects.create(user=user, FirstName=FirstNamedata, LastName=LastNamedata, Contract=Contractdata, Email=Emaildata)

            login(request, user)

            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()

    context = {"form":form}
    return render(request, "app_user/register.html", context)