from django.shortcuts import render
from django.http.response import HttpResponse
from .models import TourNames

# Create your views here.
def tours(request):
    all_tours = TourNames.objects.order_by('TourName')

    context = {'tours': all_tours}
    return render(request, 'app_tours/tours.html',context)

def tour(request, tour_name):
    one_tour = None
    try:
        one_tour = TourNames.objects.get(TourName=tour_name)
    except:
        print("ไม่พบข้อมูล")
    context = {'tour': one_tour}
    return render(request,'app_tours/tour.html', context)
