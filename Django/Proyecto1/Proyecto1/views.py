from django.http import HttpResponse # Importamos el módulo django.http para hacer peticiones

import datetime
from django.template import Template, Context

def saludo(request): # primera vista

    doc_externo = open("C:/Users/Nicolas/Desktop/Cursos/Django/Proyecto1/Proyecto1/plantillas/mi_plantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

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
