from .models import Reporte, Comentario
from .tables import ReporteTable
from .filter import ReporteFilter, ComentarioFilter
from .forms import ReporteForm, ComentarioForm
from django.urls import reverse_lazy
from django.db.models import Q

#VISTAS BASADAS EN CLASES
from django.views.generic import View,ListView,TemplateView, DetailView, DeleteView, UpdateView, CreateView
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

######### Reportes ##########
class InfoIndex(SingleTableMixin, FilterView):
    model = 'Reporte'
    table_class = ReporteTable
    template_name = 'tabla_filter.html'
    queryset = Reporte.objects.all()
    filterset_class = ReporteFilter

class ReporteCreation(CreateView):
    model = Reporte
    success_url = reverse_lazy('index')
    template_name = 'formularios/formulario.html'
    form_class = ReporteForm
    

class ReporteUpdate(UpdateView):
    model = Reporte
    success_url = reverse_lazy('index')
    form_class = ReporteForm
    template_name = 'reporte.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_variable = self.kwargs.get('pk',0)
        reporte = Reporte.objects.get(pk = pk_variable)
        context['titulo'] = reporte.titulo
        context['comentarios'] = Comentario.objects.filter(autor=reporte.pk).values()
        return context

class ReporteDelete(DeleteView):
    model = Reporte
    template_name = 'formularios/formulario_borrado.html'
    success_url = reverse_lazy('index')

####### Comentarios #######

class ComentarioCreation(CreateView):
    model = Comentario
    success_url = reverse_lazy('index')
    template_name = 'formularios/formulario_comentarios.html'
    form_class = ComentarioForm

class ComentarioUpdate(UpdateView):
    model = Comentario
    success_url = reverse_lazy('index')
    form_class = ComentarioForm
    template_name = 'formularios/formulario_comentarios.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_variable = self.kwargs.get('pk',0)
        comentario = Comentario.objects.get(pk = pk_variable)
        context['titulo'] = comentario.titulo
        context['comentarios'] = Comentario.objects.filter(autor=comentario.pk).values()
        return context

class ComentarioDelete(DeleteView):
    model = Comentario
    template_name = 'formularios/formulario_borrado_comentario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_variable = self.kwargs.get('pk',0)
        comentario = Comentario.objects.get(id = pk_variable)
        reporte_numero =  Reporte.objects.get(titulo=comentario.autor)
        context['numero_reporte'] = reporte_numero.pk
        return context