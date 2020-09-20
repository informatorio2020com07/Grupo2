from django.db import models
from cuenta.models import Perfil, Categoria

# Create your models here.

class Oferta(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="oferta/", null=True)
    oferente = models.ForeignKey(Perfil, on_delete = models.CASCADE,default=None, related_name="oferta_creados")
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_modificado = models.DateField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL,null=True)
    fecha_caducacion =models.DateField(null=True,blank=True,default=None)
    def __str__(self):
        return self.titulo
