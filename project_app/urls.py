from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('ending/',views.ending,name="ending"),
]