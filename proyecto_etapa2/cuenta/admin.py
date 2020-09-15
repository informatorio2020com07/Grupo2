from django.contrib import admin
from cuenta.models import Perfil,Perfil_trabajador,Titulo,Categoria,Matricula_Titulo
from bolsa.models import Oferta

admin.site.register(Categoria)
admin.site.register(Perfil)
admin.site.register(Perfil_trabajador)
admin.site.register(Titulo)
admin.site.register(Oferta)
admin.site.register(Matricula_Titulo)

# Register your models here.
