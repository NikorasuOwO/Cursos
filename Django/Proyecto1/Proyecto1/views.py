from django.http import HttpResponse # Importamos el módulo django.http para hacer peticiones

import datetime


def saludo(request): # primera vista

    documento = """
    <html>
    <body>
    <h1>
    Hola esta es mi primera página con Django
    </h1>
    </body>
    </html>
    """

    return HttpResponse(documento) # Respuesta a la peticion

def despedida(request):
    return HttpResponse("¡Hasta luego!")

def hora_actual(request):

    documento = """
    <html>
    <body>
    <h1>
    Fecha y hora actual: %s
    </h1>
    </body>
    </html>
    """ % datetime.datetime.now()


    return HttpResponse(documento)

def calcula_edad(request, edad, year):

    periodo = year-datetime.datetime.today().year
    edad_futura = edad + periodo
    documento = """
    <html>
    <body>
    <h2>
    En el año %s tendrás %s años.
    </h2>
    </body>
    </html>
    """ %(year, edad_futura)

    return HttpResponse(documento)
