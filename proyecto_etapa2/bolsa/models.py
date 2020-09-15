from django.db import models
from cuenta.models import Perfil_trabajador,Categoria

# Create your models here.

class Oferta(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    oferente = models.ForeignKey(Perfil_trabajador, on_delete = models.CASCADE,default=None, related_name="oferta_creados")
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL,null=True)

    def __str__(self):
        return self.titulo
