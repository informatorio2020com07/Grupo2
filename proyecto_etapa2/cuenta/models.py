from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Titulo(models.Model):
    titulo = models.CharField(max_length = 30)
    matricula = models.CharField(max_length = 30,null = True)
    def __str__(self):
        return self.titulo

class Perfil(AbstractUser):
    nacimiento = models.DateField(null = True)
    foto = models.ImageField(upload_to = "foto_perfil", null = True, blank = True)
    telefono = models.CharField(max_length = 20)
    localidad = models.CharField(max_length = 60)
    provincia = models.CharField(max_length = 30)

class Perfil_trabajador(Perfil):
    experiencia_laboral = models.CharField(max_length = 200,null = True)
    recomendaciones = models.IntegerField()
    titulo = models.ManyToManyField("Titulo", blank=True, related_name="trabajador_titulo")
    
class Categoria(models.Model):
    nombre_cat = models.CharField(max_length = 30)
    descripcion = models.TextField()
    titulo = models.ManyToManyField("Titulo", blank=True, related_name="categorias_en_titulo")
    def __str__(self):
        return self.nombre_cat

class Comentario(models.Model):
    com_trabajor = models.ForeignKey(Perfil_trabajador, on_delete = models.CASCADE, related_name="comentarios_de_trabajador")
    usuario = models.ForeignKey(Perfil, on_delete = models.SET_NULL, null = True, related_name="comentario_cliente")
    texto = models.TextField(max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now_add = True)


