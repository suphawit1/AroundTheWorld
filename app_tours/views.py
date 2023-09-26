from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Tours,Countrys
# Create your views here.
def tours(request):
    unique_regions = Countrys.objects.values('Region').distinct()
    regions_list = []
    all_tours = Tours.objects.order_by('TourName')

    for regions in unique_regions:
        for tour in all_tours:
            if tour.CountryName.Region == regions['Region']:
                regions_list.append(regions['Region'])
                break

    all_tours = Tours.objects.order_by('TourName')

    context = {'tours': all_tours,'regions':regions_list}
    return render(request, 'app_tours/tours.html',context)

def tour(request, tour_name):
    one_tour = None
    try:
        one_tour = Tours.objects.get(TourName=tour_name)
    except:
        print("ไม่พบข้อมูล")
    
    context = {'tour': one_tour}
    return render(request,'app_tours/tour.html', context)

def touredit(request, tour_name):
    one_tour = None
    
    try:
        one_tour = Tours.objects.get(TourName=tour_name)
    except:
        print("ไม่พบข้อมูล")
    
    context = {'tour': one_tour}
    return render(request,'app_tours/touredit.html', context)

