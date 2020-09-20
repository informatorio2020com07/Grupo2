from django.shortcuts import render, redirect
from .models import Oferta, Categoria
from .forms import OfertaForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    ofertas=Oferta.objects.all()  
    contexto = {"ofertas" : ofertas}
    return render(request, "bolsa/index.html",contexto)

@login_required
def new_oferta(request):
    if request.user.tipo_usuario=="trabajador":
        if request.method == "POST":
            form= OfertaForm(request.POST,request.FILES)        
            if form.is_valid():
                oferta=form.save(commit=False)
                oferta.oferente = request.user
                oferta.save()
                return redirect("oferta", oferta.id)
            else:
                contexto={"form":form,}
                return render(request, "bolsa/new.html",contexto)
        #Metodo Get        
        form = OfertaForm()
        contexto={"form":form,}
        return render(request, "bolsa/new.html",contexto)
    else:
        return redirect("index")

def show_oferta(request,id):
    oferta=Oferta.objects.get(pk=id)
    usuario=oferta.oferente
    contexto = {
    "oferta":oferta,}
    return render(request,"bolsa/oferta.html",contexto)

def show_categoria(request,id):
    cat=Categoria.objects.get(pk=id)
    print(cat.id)
    ofertas = Oferta.objects.filter(categoria=cat.id)
    print(ofertas)
    contexto = {"ofertas":ofertas,}
    return render(request, "bolsa/index.html",contexto)
