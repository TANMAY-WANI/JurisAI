from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("",views.index),
    # path("admin/", admin.site.urls),
    path("login/",views.login),
]
