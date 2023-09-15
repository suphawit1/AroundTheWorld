from django.urls import path
from . import views

urlpatterns = [
    path('',views.tours,name='tours'),
    path('<str:tour_name>',views.tour,name='tour')
]