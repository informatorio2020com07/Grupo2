from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class NuevoUsuarioForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("first_name","last_name","username","dni", "email", "password1",
         "password2", "nacimiento", "foto","telefono","experiencia_laboral","localidad",
         "titulo")
        def __init__(self, *args, **kwargs):
            super(NuevoTrabajadorForm, self).__init__(*args, **kwargs)
            self.fields["titulo"].widget.attrs.update({'class' : 'form-check-input','placeholder' : '',"id":"defaultUnchecked", 'type' : 'checkbox'})
