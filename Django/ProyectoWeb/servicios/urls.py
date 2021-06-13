
#URLs de la aplicación
from django.urls import path
from . import views # Importamos el archivo con las views (de la app servicios)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # URLs para todo el proyecto
    path('', views.servicios, name='Servicios'),
]
