from django.urls import path
from . import views

urlpatterns = [
    path("iniciar_sesion", views.iniciar_sesion, name="iniciar_sesion"),
    path("cerrar_sesion", views.cerrar_sesion, name="cerrar_sesion"),
    path("nuevo_cliente", views.nuevo_cliente, name="nuevo_cliente"),
    path("nuevo_trabajador", views.nuevo_trabajador, name="nuevo_trabajador"),
    path("perfil/editar/cargar_titulo/<int:id>", views.cargar_titulo, name="cargar_titulo"),
    path("perfil/<int:id>", views.ver_perfil, name="ver_perfil"),
    path("perfil/editar/<int:id>", views.editar_perfil, name="editar_perfil"),
    path("perfil/editar/cambiar_pass/<int:id>", views.cambiar_pass, name="cambiar_pass"),
    ]