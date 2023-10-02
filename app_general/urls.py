from django.urls import path
from . import views
from app_tours.views import tours

urlpatterns = [
    path('',tours, name='home'),
    path('booking/<str:tour_name>', views.booking, name='booking'),
    path('payment/<str:pay_num>', views.payment, name='payment')
]