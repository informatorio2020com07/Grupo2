from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import NuevoClienteForm,NuevoTrabajadorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import Perfil,Perfil_trabajador
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def nuevo_cliente(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = NuevoClienteForm()
        if request.method == "POST":
            form = NuevoClienteForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    login(request,user)
                    return redirect("index")
        return render(request, "cuenta/crear_cuenta.html",{"form":form,"pagina":"cliente"})

def nuevo_trabajador(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = NuevoTrabajadorForm()
        if request.method == "POST":
            form = NuevoTrabajadorForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    login(request,user)
                    return redirect("index")
        return render(request, "cuenta/crear_cuenta.html",{"form":form,"pagina":"trabajador"})


def iniciar_sesion(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
    return render(request, "cuenta/iniciar_sesion.html", {"form":form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("index")

@login_required
def ver_perfil(request,id):
    try:
        perfil = Perfil_trabajador.objects.get(pk=id)
    except ObjectDoesNotExist:
        perfil = Perfil.objects.get(pk=id)
    print(perfil.first_name)   
    contexto = {
        "perfil":perfil,
        }
    template = "cuenta/perfil.html"

    return render(request, template, contexto)

def index(request):
    contexto= {"H":"Hola Mundo"}
    return render(request,"cuenta/index.html",contexto)