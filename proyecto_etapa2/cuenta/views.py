from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import NuevoUsuarioForm, UpdateUsuarioForm, TerminarInscripcionForm, ComentarioForm, Search_perfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .models import (Perfil,Titulo,Categoria,
Matricula_Titulo,Recomendaciones,Comentario, Que_hacemos)
from bolsa.models import Oferta
from django.db import IntegrityError
from bolsa.views import index


def nuevo_cliente(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = NuevoUsuarioForm()
        if request.method == "POST":
            form = NuevoUsuarioForm(request.POST, request.FILES)
            if form.is_valid():
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
        categorias=Categoria.objects.all()
        if request.method == "POST":
            form = NuevoUsuarioForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save(commit=False)
                user.tipo_usuario="trabajador"
                user.save()
                if user is not None:
                    login(request,user)
                    return redirect("cargar_titulo", user.id)
        return render(request, "cuenta/crear_cuenta.html",{"form":form,"pagina":"trabajador","categorias":categorias})

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


def ver_perfil(request,id):   
    perfil = Perfil.objects.get(pk=id)
    form_comentario=ComentarioForm()
    comentarios = perfil.comentarios_de_trabajador.all().order_by("-fecha_creacion")
    ofertas=Oferta.objects.filter(oferente_id=id)
    recomendaciones=Recomendaciones.objects.filter(trabajador_id=id).count()
    matriculas = Matricula_Titulo.objects.filter(trabajador_id=id)
    contexto = {"perfil":perfil,
    "matriculas":matriculas,
    "ofertas":ofertas,
    "recomendaciones":recomendaciones,
    "form_comentario":form_comentario,
    "comentarios":comentarios
    }
    return render(request, "cuenta/perfil.html", contexto)

@login_required
def editar_perfil(request, id):
    perfil = Perfil.objects.get(pk=id)
    if perfil == request.user:
        form = UpdateUsuarioForm(instance=request.user)
        if request.method == "POST":
            form = UpdateUsuarioForm(data=request.POST, files=request.FILES, instance=request.user)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    login(request,user)
                    return redirect("ver_perfil", perfil.id)
        return render(request, "cuenta/editar_perfil.html",{"form":form,})
    else:
        return redirect("index")

@login_required
def cambiar_pass(request, id):
    perfil = Perfil.objects.get(pk=id)
    if perfil == request.user:
        form = PasswordChangeForm(user=perfil)
        if request.method == "POST":
            form = PasswordChangeForm(data=request.POST, user=perfil)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    login(request,user)
                    return redirect("ver_perfil", perfil.id)
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "cuenta/cambiar_contrasena.html",{"form":form})
    else:
        return redirect("index")


@login_required
def cargar_titulo(request,id):
    perfil = Perfil.objects.get(pk=id)
    if perfil == request.user and perfil.tipo_usuario=="trabajador":
        form = TerminarInscripcionForm(categoria=perfil.categoria.id)
        if request.method == "POST":
            form = TerminarInscripcionForm(data=request.POST,categoria=perfil.categoria.id)
            if form.is_valid():
                datos = form.cleaned_data
                if datos["titulo_nuevo"]!="" or datos["titulo"]:
                    #controla que no tenga nuevo titulo
                    if datos["titulo_nuevo"]!="":
                        bus_titu=Titulo.objects.filter(titulo__icontains=datos["titulo_nuevo"]).first()
                        if bus_titu:
                            cat=bus_titu.categoria.id
                        else:
                            bus_titu=0
                            cat=5
                    else:
                        cat=5
                        bus_titu=0
                    print(bus_titu)
                    print(cat)
                    #contrala que si hay nuevo titulo no sea de otra categoria o este cargado
                    if perfil.categoria.id==5 and cat!=5:
                        error="La Profesion es de otra categoria, Usted debe cambiar de categoria "+bus_titu.categoria.nombre_cat
                        return render(request, "cuenta/cargar_titulo.html",{"form":form,"error":error})
                    elif perfil.categoria.id==5 and cat==5 and bus_titu!=0:
                        return render(request, "cuenta/cargar_titulo.html",{"form":form,"error":"La Profesion esta arriba"})
                    
                    matricula_titulo=form.save(commit=False)
                    #si el titulo es nuevo y no esta cargado lo crea
                    if perfil.categoria.id==5 and datos["titulo_nuevo"]!="" and bus_titu==0:
                        titulo=Titulo.objects.create(titulo=datos["titulo_nuevo"],categoria_id=5)
                        matricula_titulo.titulo_id=titulo.id
                    matricula_titulo.trabajador_id=perfil.id
                    if datos["matricula"] == None:
                        matricula_titulo.matricula=""
                    #controla que no tenga dos veces el mismo titulo
                    try:
                        matricula_titulo.save()
                    except IntegrityError as e:
                        return render(request, "cuenta/cargar_titulo.html",{"form":form,"error":"Usted ya posee ese titulo si desea modificarlo borrelo"})
                    return redirect("ver_perfil", perfil.id)
        return render(request, "cuenta/cargar_titulo.html",{"form":form})
    else:
        return redirect("index")


@login_required
def borrar_titulo(request,id):
    matricula=Matricula_Titulo.objects.get(pk=id)
    if request.user.id == matricula.trabajador_id:
        matricula.delete()
        return redirect("ver_perfil", request.user.id)            
    else:
        return redirect("ver_perfil", request.user.id)

@login_required
def si_recomiendo(request, id):
    perfil = Perfil.objects.get(pk=id)
    if perfil != request.user:
        try:
            recomendaciones=Recomendaciones.objects.create(trabajador_id=perfil.id,cliente_id=request.user.id,recomendaciones=1)
        except IntegrityError as e:
            return redirect("ver_perfil", perfil.id)
    return redirect("ver_perfil", perfil.id)

@login_required
def no_recomiendo(request, id):
    perfil = Perfil.objects.get(pk=id)
    if perfil != request.user:
        try:
            recomendaciones=Recomendaciones.objects.filter(trabajador_id=perfil.id).filter(cliente_id=request.user.id)
            recomendaciones.delete()
        except IntegrityError as e:
            return redirect("ver_perfil", perfil.id)
    return redirect("ver_perfil", perfil.id)

@login_required
def comentar(request,id):
    perfil = Perfil.objects.get(pk=id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario_id = request.user.id
            comentario.com_trabajador_id = perfil.id
            try:
                comentario.save()
            except IntegrityError as e:
                return redirect("ver_perfil", perfil.id)
            return redirect("ver_perfil", perfil.id)
    else:
        return redirect("ver_perfil", perfil.id)


def search_perfil(request):
    if request.GET:
        form = Search_perfilForm(request.GET)
    else:
        form = Search_perfilForm()
    filtro_titulo = request.GET.get("titulo", None)
    filtro_localidad = request.GET.get("localidad", None)
    print(filtro_titulo)
    print(filtro_localidad)
    if filtro_titulo and filtro_localidad:
        perfiles=Perfil.objects.filter(matricula_de_trabajador__titulo__id=filtro_titulo).filter(localidad=filtro_localidad).filter(tipo_usuario="trabajador")
    elif filtro_titulo:
        perfiles=Perfil.objects.filter(matricula_de_trabajador__titulo__id=filtro_titulo).filter(tipo_usuario="trabajador")
    elif filtro_localidad:
        perfiles=Perfil.objects.filter(localidad_id=filtro_localidad).filter(tipo_usuario="trabajador")
    else:
        perfiles=None

    return render(request, "cuenta/search_perfil.html",{"form":form, "perfiles":perfiles})


@login_required
def dar_baja(request,id):
    perfil = Perfil.objects.get(pk=id)
    if perfil == request.user:
        return render(request, "cuenta/dar_baja.html",{"perfil":perfil})



@login_required
def dar_baja_definitiva(request,id):
    perfil = Perfil.objects.get(pk=id)
    if perfil == request.user:
        print("entro")
        if request.method == "POST":
            print("entro aca")
            perfil.delete()
            return redirect("index")
    return render(request, "cuenta/dar_baja.html",{"perfil":perfil})

def ayuda(request):
    contenido=Que_hacemos.objects.first()
    return render(request, "cuenta/que_hacemos.html",{"contenido":contenido})