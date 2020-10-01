from django.shortcuts import render, redirect
from .models import Oferta
from cuenta.models import Categoria
from .forms import OfertaForm,SearchForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.


def index(request):
    if request.GET:
        search_form = SearchForm(request.GET)
    else:
        search_form = SearchForm()

    filtro_titulo = request.GET.get("titulo", None)
    if filtro_titulo:
        ofertas_buscar = Oferta.objects.filter(oferente__matricula_de_trabajador__titulo__titulo__icontains=filtro_titulo)
    else:   
        ofertas_buscar=None

    if request.user.is_authenticated:
        ofertas1=Oferta.objects.filter(oferente__localidad=request.user.localidad)
    else:
        ofertas1 = None  
    ofertas=Oferta.objects.all()
    contexto = {"ofertas" : ofertas,
                "ofertas1" : ofertas1,
                "ofertas_buscar" : ofertas_buscar,
                "search_form" : search_form
                }
    return render(request, "bolsa/index.html",contexto)

@login_required
def new_oferta(request):
    if request.user.tipo_usuario=="trabajador":
        if request.user.matricula_de_trabajador.all().count()>0:
            if request.method == "POST":
                form= OfertaForm(request.POST,request.FILES)        
                if form.is_valid():
                    datos=form.cleaned_data
                    b=datetime.now()
                    
                    if (datos["fecha_caducacion"] is None) or (datos["fecha_caducacion"] > b.date()):
                        oferta=form.save(commit=False)
                        oferta.oferente = request.user  
                        oferta.categoria_id=request.user.categoria.id
                        oferta.save()
                        return redirect("oferta", oferta.id)
                    else:
                        contexto={"form":form,"error_fecha":"La fecha es vieja"}
                        return render(request, "bolsa/new.html",contexto)        
                else:
                    contexto={"form":form,}
                    return render(request, "bolsa/new.html",contexto)
            #Metodo Get        
            form = OfertaForm()
            contexto={"form":form,}
            return render(request, "bolsa/new.html",contexto)
        else:
            return redirect("cargar_titulo", request.user.id)
    else:
        return redirect("index")

def show_oferta(request,id):

    oferta=Oferta.objects.get(pk=id)
    usuario=oferta.oferente
    contexto = {
    "oferta":oferta,}
    return render(request,"bolsa/oferta.html",contexto)

def show_categoria(request,id):
    if request.GET:
        search_form = SearchForm(request.GET)
    else:
        search_form = SearchForm()

    filtro_titulo = request.GET.get("titulo", None)
    if filtro_titulo:
        ofertas_buscar = Oferta.objects.filter(oferente__matricula_de_trabajador__titulo__titulo__icontains=filtro_titulo)
    else:   
        ofertas_buscar=None
    cat=Categoria.objects.get(pk=id)
    ofertas = Oferta.objects.filter(categoria=cat.id)
    contexto = {"ofertas":ofertas,
                "search_form" : search_form}
    return render(request, "bolsa/index.html",contexto)

def borrar_oferta(request,id):
    oferta=Oferta.objects.get(pk=id)
    if oferta.oferente == request.user:
        if request.method == "POST":
            if oferta.oferente == request.user:
                oferta.delete()
                return redirect("index")            
        else:
            oferta.delete()
            return redirect("index")


def editar_oferta(request, id):
    oferta = Oferta.objects.get(pk = id)
    if oferta.oferente == request.user:
        if request.method == "GET":
            form = OfertaForm(instance = oferta)
            contexto = {
                "form" : form,
                "editar" : "editar"
            }
            return render(request, "bolsa/new.html", contexto)
        elif request.method == "POST":
            form = OfertaForm(request.POST,request.FILES, instance = oferta)
            if form.is_valid():
                datos=form.cleaned_data
                b=datetime.now()
                if datos["fecha_caducacion"]:
                    if datos["fecha_caducacion"] > b.date():
                        ofer = form.save()
                        return redirect("oferta", ofer.id)
                    else:
                        contexto={"form":form,"error_fecha":"La fecha es vieja"}
                        return render(request, "bolsa/new.html",contexto)
                else:
                    ofer = form.save()
                    return redirect("oferta", ofer.id)
                    
            else:
                contexto = {
                "form" : form,
                }
                return render(request, "bolsa/new.html", contexto)


