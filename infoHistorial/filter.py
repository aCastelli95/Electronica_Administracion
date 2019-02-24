import django_filters
from .models import Reporte

class ReporteFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    fecha = django_filters.DateFilter(lookup_expr='lte')

    class Meta:
        model = Reporte
        fields = ['titulo', 'fecha',]