from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", view= views.register, name= "register"),
    path("dashboard", view= views.dashboard_user, name= "dashboard_user"),
    path("bokinglist", view= views.dashboard_book, name= "dashboard_book")
]