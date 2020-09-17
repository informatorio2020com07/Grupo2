from django.shortcuts import render, redirect
from .models import Oferta, Categoria
from .forms import OfertaForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    contexto = {}
    return render(request, "bolsa/index.html",contexto)

#@login_required
def new_oferta(request):
    if request.method == "POST":
        form= OfertaForm(request.POST,request.FILES)
        print(form)
        lista=request.user.titulo
        categorias=Categorias.Object.filter(titulo__in=lista)
        if form.is_valid():
            oferta=form.save(commit=False)
            oferta.oferente = request.user
            print("llego")
            oferta.save()
            return redirect("oferta", oferta.id)
        else:
            contexto={"form":form,}
            return render(request, "bolsa/new.html",contexto)
    form = OfertaForm()
    contexto={"form":form,}
    return render(request, "bolsa/new.html",contexto)

def show_oferta(request,id):
    oferta=Oferta.objects.get(pk=id)
    usuario=oferta.oferente
    contexto = {
    "oferta":oferta,}
    return render(request,"bolsa/oferta.html",contexto)

def show_categoria(request,id):
    categorias = Categoria.objects.all()
    cat=Categoria.objects.get(pk=id)
    oferta = Oferta.objects.filter(categoria=cat)
    contexto = {"oferta":oferta,}
    return render(request, "bolsa/index.html",contexto)
    