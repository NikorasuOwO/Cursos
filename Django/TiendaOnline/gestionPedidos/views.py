from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    #mensaje="Artículo buscado: " + str(request.GET["producto"])
    if request.GET.get('producto'):
        #mensaje = f"Artículo buscado: {request.GET.get('producto','')}"
        producto = request.GET.get('producto')
        if(len(producto) > 20):
            mensaje="Texto de búsqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})

    else:
        producto = "No has introducido nada :("

    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":
        return render(request, "gracias.html")

    return render(request, "contacto.html")
