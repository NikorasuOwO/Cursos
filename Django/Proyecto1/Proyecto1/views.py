from django.http import HttpResponse # Importamos el módulo django.http para hacer peticiones

def saludo(request): # primera vista
    return HttpResponse("Hola esta es nuestra primera página con Django") # Respuesta a la peticion

def despedida(request):
    return HttpResponse("¡Hasta luego!")
