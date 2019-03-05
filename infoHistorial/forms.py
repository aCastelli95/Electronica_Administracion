from django import forms
from .models import Reporte, Comentario
from django.core.exceptions import NON_FIELD_ERRORS
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

class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = '__all__'
        widgets = {
            'autor': forms.Select(
                attrs={'class':'js-example-theme-single form-control',
                        'title':'Autor',
                        }),
                           
        }
        
       