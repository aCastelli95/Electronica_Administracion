import django_tables2 as tables
from .models import Reporte

class ReporteTable(tables.Table):
    
    class Meta:
        model = Reporte
        template_name = 'django_tables2/bootstrap.html'