from django.shortcuts import render
from django.views.generic import ListView
from django.urls import include, path
from infoHistorial.views import InfoIndex

# Create your views here.
urlpatterns = [
    path('', InfoIndex.as_view(), name='index'),
]