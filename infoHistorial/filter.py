import django_filters
from .models import Reporte, Comentario

class ReporteFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    modelo = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Reporte
        fields = ['titulo', 'modelo',]

class ComentarioFilter(django_filters.FilterSet):
    autor = django_filters.CharFilter(lookup_expr='icontains')
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    fecha = django_filters.DateFilter(lookup_expr='lte')
    
    class Meta:
        model = Comentario
        fields = ['autor','titulo','fecha',]