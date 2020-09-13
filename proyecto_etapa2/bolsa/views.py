from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    contexto= {"H":"Hola Mundo"}
    return render(request,"bolsa/index.html",contexto)