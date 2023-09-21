from django.urls import path
from . import views

urlpatterns = [
    path("login", view= views.loginview, name= "login"),
    path('logout/', views.logoutview, name='logout'),
    path("register", view= views.register, name= "register"),
    path("dashboard", view= views.dashboard_user, name= "dashboard_user"),
    path("bokinglist", view= views.dashboard_book, name= "dashboard_book")
]