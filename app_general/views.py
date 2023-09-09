from django.shortcuts import render
from django.http.response import HttpResponse
from app_tours.models import TourNames

# Create your views here.
def home(request):
    return render(request,'app_general/home.html')

def booking(request):
    all_tours = TourNames.objects.order_by('TourName')
    context = {'tours': all_tours}
    return render(request,'app_general/booking_forms.html', context)
