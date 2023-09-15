from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/<str:tour_name>', views.booking, name='booking'),
    path('payment/<str:pay_num>', views.payment, name='payment')
]