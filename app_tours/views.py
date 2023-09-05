from django.shortcuts import render
from django.http.response import HttpResponse


all_tours = [
    {'id': 1, 'title':'Bankok','country': 'Thailand'},
    {'id': 2, 'title':'Tokyo','country': 'Japan'},
    {'id': 3, 'title':'Somewhere','country': 'Thailand'}
]

# Create your views here.
def tours(request):
    context = {'tours': all_tours}
    return render(request, 'app_tours/tours.html',context)

def tour(request, tour_id):
    one_tour = None
    try:
        one_tour = [f for f in all_tours if f['id'] == tour_id][0]
    except IndexError:
        print('ไม่พบข้อมูล')
    context = {'tour': one_tour}
    return render(request,'app_tours/tour.html', context)
