from django.urls import path
from . import views

urlpatterns = [
    path("login", view= views.loginview, name= "login"),
    path('logout/', views.logoutview, name='logout'),
    path("register", view= views.register, name= "register"),
    path("profile", view= views.profile, name= "profile")
]