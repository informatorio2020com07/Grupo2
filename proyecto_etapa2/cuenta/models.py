from django.db import models
from django.contrib.auth.models import AbstractUser
from bolsa.models import Categoria
# Create your models here.

class Provincia(models.Model):
    provincia = models.CharField(max_length = 30)

class Localidad(models.Model):
    localidad = models.CharField(max_length = 30)
    provincia = models.ForeignKey(Provincia, on_delete = models.CASCADE,default=None, related_name="personas_provincia")

class Titulo(models.Model):
    titulo = models.CharField(max_length = 30)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE,default=None, related_name="titulo_de_categoria")
    def __str__(self):
        return self.titulo

class Perfil(AbstractUser):
    nacimiento = models.DateField(null = True)
    foto = models.ImageField(upload_to = "foto_perfil", null = True, blank = True)
    telefono = models.CharField(max_length = 20)
    localidad = models.ForeignKey(Localidad, on_delete = models.CASCADE,default=None,null=True, related_name="personas_localidad") 
    def __str__(self):
        return self.username

class Perfil_trabajador(Perfil):
    experiencia_laboral = models.CharField(max_length = 200,null = True)
    recomendaciones = models.IntegerField(default=0)
    titulo = models.ManyToManyField(Titulo, blank=True, through="Matricula_Titulo", related_name="matricula_perfilT")

class Matricula_Titulo(models.Model):
    trabajador = models.ForeignKey(Perfil_trabajador, on_delete = models.SET_NULL, null = True, related_name="matricula_de_trabajador")
    titulo = models.ForeignKey(Titulo, on_delete = models.CASCADE,default=None, related_name="matricula_de_titulo")
    matricula = models.CharField(max_length = 30,null = True)

class Comentario(models.Model):
    com_trabajor = models.ForeignKey(Perfil_trabajador, on_delete = models.CASCADE, related_name="comentarios_de_trabajador")
    usuario = models.ForeignKey(Perfil, on_delete = models.SET_NULL, null = True, related_name="comentario_cliente")
    texto = models.TextField(max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now_add = True)


