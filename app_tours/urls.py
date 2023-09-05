from django.urls import path
from . import views

urlpatterns = [
    #<int:tour_id> ส่งไป view
    path('',views.tours,name='tours'),
    path('<int:tour_id>',views.tour,name='tour')
]