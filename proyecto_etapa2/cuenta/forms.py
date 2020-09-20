from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Perfil,Titulo,Localidad,Matricula_Titulo,Categoria
from phone_field import PhoneField

class NuevoUsuarioForm(UserCreationForm,forms.Form):
    localidad=forms.ModelChoiceField(queryset=Localidad.objects.all().order_by("localidad"))
    username=forms.CharField(initial="", widget=forms.TextInput(attrs={"placeholder":"Nombre de usuario"}))
    dni=forms.IntegerField(max_value=99999999)
    first_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nombre"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Apellido"}))
    email=forms.EmailField(initial="",widget=forms.TextInput(attrs={"placeholder":"Correo Electronico"}))
    password1=forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2=forms.CharField(max_length=32, widget=forms.PasswordInput)
    nacimiento=forms.DateField(widget=forms.TextInput(attrs={"placeholder":"01/01/1000"}))
    foto=forms.ImageField()
    telefono= forms.CharField(help_text='Numero de Contacto')
    class Meta:
        model = Perfil
        fields = ("first_name","last_name","username","dni", "email", "password1",
         "password2", "nacimiento", "foto","telefono","localidad")

class UpdateUsuarioForm(UserChangeForm):
    experiencia_laboral=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Tu forma de trabajar en 200 caracteres"}))
    categoria=forms.ModelChoiceField(queryset=Categoria.objects.all(),initial="1")
    titulo = forms.ModelChoiceField(queryset=Titulo.objects.all(),
        widget=forms.CheckboxSelectMultiple,required = False)
    matricula=forms.CharField()
    class Meta:
        model = Perfil
        fields = ("email","foto","telefono","experiencia_laboral","localidad",
        "categoria","titulo","matricula")