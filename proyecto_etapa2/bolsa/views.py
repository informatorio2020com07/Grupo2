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
    categorias = Categoria.objects.all()
    cat=Categoria.objects.get(pk=id)
    oferta = Oferta.objects.filter(categoria=cat)
    contexto = {"oferta":oferta,}
    return render(request, "bolsa/index.html",contexto)

def borrar_oferta(request,id):
    oferta=Oferta.objects.get(pk=id)
    print(oferta)
    print(request.method)
    if request.method == "POST":
        print("es post")
        if oferta.oferente == request.user:
            oferta.delete()
            print(request.user,"gggggggggggggggggggggggggggggggggggggggggggggggg")
            #return redirect("show_oferta",request.user.id)
            return redirect("index")            
    else:
        print("no es post es get")
        oferta.delete()
        return redirect("index")

def editar_oferta(request, id):
    oferta = Oferta.objects.get(pk = id)

    if request.method == "GET":
        form = OfertaForm(instance = oferta)
        contexto = {
            "form" : form
        }
        return render(request, "bolsa/new.html", contexto)

    elif request.method == "POST":
        form = OfertaForm(request.POST, instance = oferta)
        if form.is_valid():
            ofer = form.save()
            return redirect("oferta", ofer.id)


