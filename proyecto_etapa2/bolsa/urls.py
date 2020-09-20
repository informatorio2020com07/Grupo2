from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("oferta/<int:id>", views.show_oferta, name="oferta"),
path("oferta/new", views.new_oferta,name="new_oferta"),
path("oferta/categoria/<int:id>", views.show_categoria,name="show_categoria"),
path("oferta/<int:id>/borrar", views.borrar_oferta, name="borrar_oferta"),
path("oferta/<int:id>/editar", views.editar_oferta, name="editar_oferta"),
]
