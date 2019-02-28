from .models import Reporte 
from .tables import ReporteTable
from .filter import ReporteFilter
from .forms import ReporteForm
from django.urls import reverse_lazy

#VISTAS BASADAS EN CLASES
from django.views.generic import View,ListView,TemplateView, DetailView, DeleteView, UpdateView, CreateView
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

class InfoIndex(SingleTableMixin, FilterView):
    model = 'Reporte'
    table_class = ReporteTable
    template_name = 'tabla_filter.html'
    queryset = Reporte.objects.all()

    filterset_class = ReporteFilter

class ReporteCreation(CreateView):
    model = Reporte
    success_url = reverse_lazy('index')
    template_name = 'formulario.html'
    form_class = ReporteForm

class ReporteUpdate(UpdateView):
    model = Reporte
    success_url = reverse_lazy('index')
    fields = ['titulo', 'fecha']
    template_name = 'formulario.html'


class ReporteDelete(DeleteView):
    model = Reporte
    success_url = reverse_lazy('infoHistorial:index')
   
    