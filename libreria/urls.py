from django.urls import path

from . import views


urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('inicio', views.inicio,name='iniciob'),
    path('nosotros', views.contacto ,name='nosotros'), #accedemos a nosotros, views.
    #(el nombre de la funcion en el views), name= el que queramos normalmente 
    #el mismo que pongamos en el path
    path('libros', views.libros, name='libros')
]