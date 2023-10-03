from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Tours,Countrys
from django.urls import reverse
import ast
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

    detail = one_tour.Detail
    if detail != "" and detail != 'undefined' and detail != None :
        head = detail.split("<<Head>>")
        headDetail = head[0].split(",,")
        Headweb = {
        'tourWeb': headDetail[0],
        'tourNameWeb' : headDetail[1],
        'tourTravelWeb' : headDetail[2],
        'tourTypeWeb' : headDetail[3],
        'tourAirlineWeb' : headDetail[4],
        'tourDurationsWeb' : headDetail[5],
        'tourPriceWeb' : headDetail[6],
        'tourHighlightWeb' :  headDetail[7],
        }
        day = head[1].split("<<Day>>")
        eachDay = day[0].split("||")
        daylist = []
        for i in eachDay:
            value = i.split(",,")
            daylist.append([value[0],value[1]])
        
        my_list = ast.literal_eval(day[1])
        time_dict = {}
        detail_dict = {}
        time_list = []

        n = 0
        for i in my_list:
            n += 1
            for j in i:
                time_list.append(j[0])
                detail_dict[str(j[0])+"||"+str(n)] = j[1]
            time_dict[n] = time_list
            time_list = []
    else:
        Headweb = {
        'tourWeb': "",
        'tourNameWeb' : "",
        'tourTravelWeb' : "",
        'tourTypeWeb' : "",
        'tourAirlineWeb' : "",
        'tourDurationsWeb' : "",
        'tourPriceWeb' : "",
        'tourHighlightWeb' :  "",
        }
        daylist = ""
        time_dict = ""
        detail_dict = ""


    context = {'tour': one_tour,'Head':Headweb,'Day':daylist,'time':time_dict,'detail':detail_dict}
    return render(request,'app_tours/tour.html', context)

def touredit(request, tour_name):
    one_tour = None
    try:
        one_tour = Tours.objects.get(TourName=tour_name)
    except:
        print("ไม่พบข้อมูล")
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            one_tour.immage = uploaded_file
        received_data = request.POST.get('data')
        one_tour.Detail = received_data
        one_tour.save()
        return HttpResponseRedirect(reverse('tour', args=[tour_name]))
    else:
        context = {'tour': one_tour}
        return render(request,'app_tours/touredit.html', context)
