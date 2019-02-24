from .models import Reporte 

#VISTAS BASADAS EN CLASES
from django.views.generic import View,ListView,TemplateView, DetailView, FormView, UpdateView, CreateView

class InfoIndex(ListView):
    model = 'Reporte'
    queryset = Reporte.objects.all()
    context_object_name = 'reporte'
    template_name = 'index.html'
