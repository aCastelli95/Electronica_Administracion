from django.db import models
from django.utils import timezone


# Create your models here.
class Reporte(models.Model):
    titulo = models.CharField(null=False, blank=False ,unique=True, max_length=20)
    fecha = models.DateTimeField(blank=True, null=True, default=timezone.now)
    archivo = models.FileField(null=True,blank=True, upload_to='archivos/')
    imagen = models.ImageField(null= True,blank=True, upload_to='imagenes/') 

    def __str__(self):
        return self.titulo
    def __unique__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.ForeignKey('Reporte', on_delete=models.CASCADE)
    titulo = models.CharField(null=False, max_length=10)
    texto = models.TextField(null=False)
    fecha = models.DateTimeField(null=False, blank = False, default=timezone.now)
    imagen = models.ImageField(null=True, blank=True, upload_to='imagenes/')

    def __str__(self):
        return self.titulo
        
    def __unique__(self):
        return self.titulo
      
