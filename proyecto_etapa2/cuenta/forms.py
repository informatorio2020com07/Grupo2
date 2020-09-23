from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Perfil,Titulo,Localidad,Matricula_Titulo,Categoria

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
    foto=forms.ImageField(required=False)
    telefono= forms.CharField(help_text='Numero de Contacto', widget=forms.TextInput(attrs={"placeholder":"codigo numero"}))
    categoria=forms.ModelChoiceField(required=False, queryset=Categoria.objects.all(),initial="1")
    experiencia_laboral=forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Tu forma de trabajar en 200 caracteres"}))
    facebook=forms.CharField(required=False)
    instagram=forms.CharField(required=False)
    class Meta:
        model = Perfil
        fields = ("first_name","last_name","username","dni", "email", "password1",
         "password2", "nacimiento", "foto","telefono","localidad","categoria","experiencia_laboral","facebook","instagram")

class UpdateUsuarioForm(UserChangeForm):
    class Meta:
        model = Perfil
        fields = ("username","email","foto","telefono","experiencia_laboral","localidad")
    def __init__(self,*args, **kwargs):
        super(UpdateUsuarioForm, self).__init__(*args, **kwargs)
        localidad=forms.ModelChoiceField(queryset=Localidad.objects.all().order_by("localidad"))
        self.fields["localidad"]=localidad
        experiencia_laboral=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Tu forma de trabajar en 200 caracteres"}))
        self.fields["experiencia_laboral"]=experiencia_laboral

class TerminarInscripcionForm(forms.ModelForm):
    class Meta:
        model = Matricula_Titulo
        fields=("matricula","titulo")
    def __init__(self,categoria, *args, **kwargs):
        super(TerminarInscripcionForm, self).__init__(*args, **kwargs)
        titulo=forms.ModelChoiceField(queryset = Titulo.objects.filter(categoria_id = categoria),widget=forms.RadioSelect,required = False)
        self.fields["titulo"]=titulo