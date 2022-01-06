
from django.contrib import admin
from django.urls import path
import apps.home.views as views

urlpatterns = [
    path("api/", views.insertLog),
    path("", views.index)
]