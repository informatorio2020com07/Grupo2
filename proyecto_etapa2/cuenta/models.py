from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Perfil(AbstractUser):
    nacimiento = models.DateField(null = True)
    foto = models.ImageField(upload_to = "foto_perfil", null = True, blank = True)
    localidad = models.CharField(max_length = 60)
    provincia = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 20)

class Perfil_trabajador(Perfil):
    experiencia_laboral = models.CharField(max_length = 200,null = True)
    recomendaciones = models.IntegerField()
    titulo = models.ManyToManyField("Perfil", blank=True, related_name="mis_titulos")
    
class Titulo(models.Model):
    titulo = models.CharField(max_length = 30)
    matricula = models.CharField(max_length = 30,null = True)
    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nombre_cat = models.CharField(max_length = 30)
    descripcion = models.TextField()
    titulo = models.ManyToManyField("Perfil", blank=True, related_name="titulos_categoria")
    def __str__(self):
        return self.nombre_cat

class Comentario(models.Model):
    com_trabajor = models.ForeignKey(Perfil_trabajador, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Perfil, on_delete = models.SET_NULL, null = True)
    texto = models.TextField(max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now_add = True)


