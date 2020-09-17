from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import NuevoUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import Perfil
from django.core.exceptions import ObjectDoesNotExist
from bolsa.views import index

# Create your views here.
def nuevo_cliente(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = NuevoUsuarioForm()
        if request.method == "POST":
            form = NuevoUsuarioForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                print("entro aca")
                user = form.save(commit=False)
                user.tipo_usuario="cliente"
                user.save()
                if user is not None:
                    login(request,user)
                    return redirect("index")
        return render(request, "cuenta/crear_cuenta.html",{"form":form,"pagina":"cliente"})

def nuevo_trabajador(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = NuevoUsuarioForm()
        if request.method == "POST":
            form = NuevoUsuarioForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                user = form.save(commit=False)
                user.tipo_usuario="trabajador"
                user.save()
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
    perfil = Perfil.objects.get(pk=id)
    contexto = {"perfil":perfil,}
    return render(request, "cuenta/perfil.html", contexto)




