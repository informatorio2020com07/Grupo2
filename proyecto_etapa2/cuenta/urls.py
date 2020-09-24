from django.urls import path

#from django.contrib.auth import views as auth_views
from . import views

from django.contrib import admin

from django.urls import path, include

from django.contrib.auth import views as auth_views,login

from django.contrib.auth.views import(

    PasswordResetView,

    PasswordResetDoneView,

    PasswordResetConfirmView,

    PasswordResetCompleteView

)


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
	
	path('reset/restablecer_pass/',PasswordResetView.as_view(template_name="restablecer_pass.html"),name="restablecer_pass"),
    path('reset/restablecer_pass_email/',PasswordResetDoneView.as_view(template_name="restablecer_pass_email.html"),name="restablecer_pass_email"),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="restablecer_pass_form.html"),name="restablecer_pass_form"),
    path('reset/restablecer_pass_complete',PasswordResetCompleteView.as_view(template_name="restablecer_pass_complete.html"),name="restablecer_pass_complete"),

    ]