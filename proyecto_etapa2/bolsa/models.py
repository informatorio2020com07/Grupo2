from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_cat = models.CharField(max_length = 30)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre_cat