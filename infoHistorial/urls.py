from django.shortcuts import render
from django.views.generic import ListView
from django.urls import include, path
from django.conf.urls import url
from infoHistorial.views import *

# Create your views here.
urlpatterns = [
    path('', InfoIndex.as_view(), name='index'),
    url(r'^nuevo$', ReporteCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ReporteUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ReporteDelete.as_view(), name='delete'),
    
    url(r'^nuevo_comentario$', ComentarioCreation.as_view(), name='new_comentario'),
    url(r'^editar_comentario/(?P<pk>\d+)$', ComentarioUpdate.as_view(), name='edit_comentario'),
    url(r'^borrar_comentario/(?P<pk>\d+)$', ComentarioDelete.as_view(), name='delete_comentario'),

    

]