from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validar_num
# Create your models here.

class Provincia(models.Model):
    provincia = models.CharField(max_length = 30)
    def __str__(self):
        return self.provincia

class Localidad(models.Model):
    localidad = models.CharField(max_length = 30)
    provincia = models.ForeignKey(Provincia, on_delete = models.CASCADE,default=None, related_name="personas_provincia")
    def __str__(self):
        return self.provincia.provincia+" - "+self.localidad

class Categoria(models.Model):
    nombre_cat = models.CharField(max_length = 30)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre_cat

class Titulo(models.Model):
    titulo = models.CharField(max_length = 30)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE,default=None, related_name="titulo_de_categoria")
    def __str__(self):
        return self.titulo

class Perfil(AbstractUser):
    tipo_usuario=models.CharField(max_length=20,default="cliente")
    dni=models.CharField(max_length=10,unique=True,default="",validators=[validar_num])
    nacimiento = models.DateField(null = True)
    foto = models.ImageField(upload_to = "foto_perfil", null = True, blank = True)
    telefono = models.CharField(max_length = 20,validators=[validar_num])
    localidad = models.ForeignKey(Localidad, on_delete = models.CASCADE, null=True, related_name="personas_localidad") 
    experiencia_laboral = models.CharField(max_length = 200,null = True, blank = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, default=None, null=True, related_name="perfil_de_categoria")
    facebook = models.CharField(max_length = 40, null=True)
    instagram = models.CharField(max_length = 40, null=True, blank = True)
    recomendaciones = models.ManyToManyField("Perfil", blank=True, through="Recomendaciones", related_name="trabajador_recomendado") 
    def __str__(self):
        return self.username

class Matricula_Titulo(models.Model):
    trabajador = models.ForeignKey(Perfil, on_delete = models.SET_NULL, null = True, related_name="matricula_de_trabajador")
    titulo = models.ForeignKey(Titulo, on_delete = models.CASCADE,null = True, related_name="matricula_de_titulo")
    matricula = models.CharField(max_length = 30,null = True, blank=True)
    class Meta:
        unique_together = ("trabajador","titulo")
    def __str__(self):
        return self.matricula

class Comentario(models.Model):
    com_trabajador = models.ForeignKey(Perfil, on_delete = models.CASCADE, related_name="comentarios_de_trabajador")
    usuario = models.ForeignKey(Perfil, on_delete = models.SET_NULL, null = True, related_name="comentario_cliente")
    texto = models.TextField(max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now_add = True)

class Recomendaciones(models.Model):
    trabajador = models.ForeignKey(Perfil, on_delete = models.SET_NULL, null = True, related_name="recomendado")
    cliente = models.ForeignKey(Perfil, on_delete = models.SET_NULL, null = True, related_name="cliente_recomendante")
    recomendaciones = models.IntegerField(default=0, null = True, blank=True)
    class Meta:
        unique_together = ("trabajador","cliente")
    def __str__(self):
        return self.recomendaciones

class Que_hacemos(models.Model):
    que_es = models.TextField(max_length=300,default="")
    que_permite = models.TextField(max_length=300,default="")
    porque_nosotros = models.TextField(max_length=300,default="")


