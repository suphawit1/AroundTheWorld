from django.urls import path
from . import views

urlpatterns = [
    #<int:tour_id> ส่งไป view
    path('',views.tours,name='tours'),
    path('<str:tour_name>',views.tour,name='tour')
]