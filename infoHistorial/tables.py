import django_tables2 as tables
from .models import Reporte
from django_tables2.utils import A
from django.utils.safestring import mark_safe

class ReporteTable(tables.Table):
    Editar = tables.LinkColumn('edit', text=mark_safe(
    '<i class="fas fa-edit"></i>'), args=[A('pk')], orderable=False)
    Borrar = tables.LinkColumn('delete', text=mark_safe(
    '<i class="fas fa-trash"></i>'), args=[A('pk')], orderable=False)
    class Meta:
        model = Reporte
        template_name = 'django_tables2/bootstrap.html'
        