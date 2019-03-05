from .models import Reporte, Comentario
from .tables import ReporteTable
from .filter import ReporteFilter, ComentarioFilter
from .forms import ReporteForm
from django.urls import reverse_lazy
from django.db.models import Q

#VISTAS BASADAS EN CLASES
from django.views.generic import View,ListView,TemplateView, DetailView, DeleteView, UpdateView, CreateView
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

#REPORTE
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
    form_class = ReporteForm
    template_name = 'formulario.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_variable = self.kwargs.get('pk',0)
        reporte = Reporte.objects.get(pk = pk_variable)
        context['titulo'] = reporte.titulo
        context['comentarios'] = Comentario.objects.filter(autor=reporte.pk).values()
        return context



class ReporteDelete(DeleteView):
    model = Reporte
    template_name = 'formulario_borrado.html'
    success_url = reverse_lazy('index')

