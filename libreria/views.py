from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html') 

def contacto(request):
    return render(request,'paginas/nosotros.html') #BUSCA EN LOS TEMPLATES

def libros(request):   
    return render(request,'libros/index.html')
