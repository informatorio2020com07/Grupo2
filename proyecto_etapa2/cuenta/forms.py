from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil,Perfil_trabajador

class NuevoClienteForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("first_name","last_name","username", "email", "password1",
         "password2", "nacimiento", "foto","telefono","localidad","provincia")

class NuevoTrabajadorForm(UserCreationForm):
    class Meta:
        model = Perfil_trabajador
        fields = ("first_name","last_name","username", "email", "password1",
         "password2", "nacimiento", "foto","telefono","localidad","provincia",
         "experiencia_laboral","titulo")