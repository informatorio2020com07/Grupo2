from django.shortcuts import render, redirect
from .models import Oferta, Categoria
from .forms import OfertaForm,OcategoriaForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    filtro_titulo = request.GET.get("param_titulo", "")
    orden_oferta = request.GET.get("param_orden", None)
    ofertas = Oferta.objects.filter(titulo__icontains = filtro_titulo)

    if orden_oferta == "titulo":
        ofertas = ofertas.order_by("titulo")
    elif orden_oferta == "antiguo":
        ofertas= ofertas.order_by("fecha_creado")
    elif orden_oferta == "nuevo":
        ofertas= ofertas.order_by("-fecha_creado")
    else:
        ofertas= ofertas.order_by("-fecha_creado")

    ocategorias = Categoria.objects.all()
    contexto = {"ofertas":ofertas,
                "categorias":ocategorias,
                "param_titulo":filtro_titulo,
                "param_orden":orden_oferta,
                                }
    return render(request, "bolsa/index.html",contexto)

#@login_required
def new_oferta(request):
    categoria = Categoria.objects.all()
    if request.method == "POST":
        form= OfertaForm(request.POST,request.FILES)
        if form.is_valid():
            oferta=form.save(commit=False)
            oferta.usuario = request.user
            oferta.save()
            return redirect("oferta", oferta.id)
        else:
            contexto={"form":form,
            "categorias":categoria}
            return render(request, "bolsa/new.html",contexto)
    form = OfertaForm()
    contexto={"form":form,
    "categorias":categoria,}
    return render(request, "bolsa/new.html",contexto)

def show_oferta(request,id):
    oferta=Oferta.objects.get(pk=id)
    usuario=oferta.oferente
    ocategorias = Categoria.objects.all()
    #mas_oferta = Oferta.objects.filter(usuario_id=usuario)
    contexto = {
    #"mas_post":mas_oferta,
    "oferta":oferta,
    "categorias":ocategorias,
    }
    return render(request,"bolsa/oferta.html",contexto)
    