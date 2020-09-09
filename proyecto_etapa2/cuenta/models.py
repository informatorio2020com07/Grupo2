from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Perfil(AbstractUser):
    nacimiento = models.DateField(null = True)
    foto = models.ImageField(upload_to = "foto_perfil", null = True, blank = True)
    permitir_comentar = models.BooleanField(default = True)

class Perfil_trabajador(Perfil):
    experiencia_laboral = models.CharField(max_length = 200,null = True)
    recomendaciones = models.IntegerField()
    #este campo remplaza la tabla
    titulo = models.ManyToManyField(Titulo, on_delete = models.CASCADE)

#esta clase desaparece
class Titulo_trabajador(models.Model):
    trabajor = models.ForeignKey(Perfil_trabajador, on_delete = models.CASCADE)
    titulo = models.ForeignKey(Titulo, on_delete = models.CASCADE) 
    
class Titulo(models.Model):
    titulo = models.CharField(max_length = 30)
    matricula = models.CharField(max_length = 30,null = True)

class Categoria(models.Model):
    nombre_cat = models.CharField(max_length = 30)
    descripcion = models.TextField()
    titulo = models.ForeignKey(Titulo, on_delete = models.CASCADE) 
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    com_trabajor = models.ForeignKey(Perfil_trabajador, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Perfil, on_delete = models.SET_NULL, null = True)
    texto = models.TextField(max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now_add = True)


