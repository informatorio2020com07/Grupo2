from django.shortcuts import render, redirect
from .models import Oferta, Categoria, Perfil_trabajador
from .forms import OfertaForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    ofertas=Oferta.objects.all()  
    contexto = {"ofertas" : ofertas}
    return render(request, "bolsa/index.html",contexto)

#@login_required
def new_oferta(request):
    if request.method == "POST":
        form= OfertaForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            print("formulario valido",form)
            oferta=form.save(commit=False)
            oferta.oferente = Perfil_trabajador.objects.first()
            
            oferta.save()
            return redirect("oferta", oferta.id)
        else:
            print("formulario valido",form)
            contexto={"form":form,
            "categorias":Categoria}
            return render(request, "bolsa/new.html",contexto)
    form = OfertaForm()
    contexto={"form":form,}
    return render(request, "bolsa/new.html",contexto)

def show_oferta(request,id):
    oferta=Oferta.objects.get(pk=id)
    usuario=oferta.oferente
    #mas_oferta = Oferta.objects.filter(usuario_id=usuario)
    contexto = {
    #"mas_post":mas_oferta,
    "oferta":oferta,}
    return render(request,"bolsa/oferta.html",contexto)
    
def lista_oferta(request): 
    ofertas=Oferta.objects.all()  
    contexto = {"ofertas" : ofertas}
    return render(request, "bolsa/lista_oferta.html", contexto)