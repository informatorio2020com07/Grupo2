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
    path("perfil/editar/borrar_titulo/<int:id>", views.borrar_titulo, name="borrar_titulo"),
    path("perfil/si_recomiendo/<int:id>", views.si_recomiendo, name="si_recomiendo"),
    path("perfil/no_recomiendo/<int:id>", views.no_recomiendo, name="no_recomiendo"),
    path("perfil/<int:id>/comentar", views.comentar, name="comentar"),
    path("search_perfil/", views.search_perfil, name="search_perfil"),
    path("perfil/dar_baja/<int:id>", views.dar_baja, name="dar_baja"),
    path("perfil/dar_baja_definitiva/<int:id>", views.dar_baja_definitiva, name="dar_baja_definitiva"),
    path("ayuda", views.ayuda, name="ayuda"),
    ]