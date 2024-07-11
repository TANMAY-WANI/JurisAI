from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("",views.index),
    path("auth/Login/",views.login_user),
    path("auth/SignUp/",views.signup_user),
    path("auth/Logout/",views.logout_user)
]
