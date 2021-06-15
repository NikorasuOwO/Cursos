
#URLs de la aplicación
from django.urls import path
from . import views # Importamos el archivo con las views


urlpatterns = [ # URLs para todo el proyecto
    path('', views.contacto, name="Contacto"),
]
