from django.contrib import admin
from django.urls import path
from Service import views

urlpatterns = [
    path('chat/',views.chat),
    path('chat_handler/',views.get_summary)
]