from .models import Reporte 
from .tables import ReporteTable
from .filter import ReporteFilter

#VISTAS BASADAS EN CLASES
from django.views.generic import View,ListView,TemplateView, DetailView, FormView, UpdateView, CreateView
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

class InfoIndex(SingleTableMixin, FilterView):
    model = 'Reporte'
    table_class = ReporteTable
    template_name = 'tabla_filter.html'
    queryset = Reporte.objects.all()

    filterset_class = ReporteFilter