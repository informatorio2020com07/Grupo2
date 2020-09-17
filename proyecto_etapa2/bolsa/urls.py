from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("oferta/<int:id>", views.show_oferta, name="oferta"),
path("oferta/new", views.new_oferta,name="new_oferta"),
path("categoria/<int:id>", views.show_categoria,name="show_categoria"),

]
