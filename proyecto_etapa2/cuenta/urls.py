from django.urls import path
from . import views

urlpatterns = [
    path("iniciar_sesion", views.iniciar_sesion, name="iniciar_sesion"),
    path("cerrar_sesion", views.cerrar_sesion, name="cerrar_sesion"),
    path("nuevo_cliente", views.nuevo_cliente, name="nuevo_cliente"),
    path("nuevo_trabajador", views.nuevo_trabajador, name="nuevo_trabajador"),
    path("perfil/<int:id>", views.ver_perfil, name="ver_perfil"),
    ]