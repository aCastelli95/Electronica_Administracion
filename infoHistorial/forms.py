from django import forms
from .models import Reporte

class ReporteForm(forms.ModelForm):

    class Meta:
        model = Reporte
        fields = '__all__'
        labels = {
            'titulo':'Titulo',
            'fecha':'Fecha', 
            'archivo':'Archivo',
            'imagen':'Imagen',
        }
       