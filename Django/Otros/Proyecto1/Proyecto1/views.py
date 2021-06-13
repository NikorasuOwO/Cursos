from django.http import HttpResponse # Importamos el módulo django.http para hacer peticiones

import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): # primera vista

    p1 = Persona("Srto. Nicolás", "Bermell")
    fecha = datetime.datetime.now()
    doc_externo = open("C:/Users/Nicolas/Desktop/Cursos/Django/Proyecto1/Proyecto1/plantillas/mi_plantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":fecha}) # Almacena un diccionario

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
