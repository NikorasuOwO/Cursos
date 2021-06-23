
#URLs de la aplicación
from django.urls import path
from . import views

urlpatterns = [ # URLs para todo el proyecto),
    path('', views.tienda, name="Tienda"), #domain/
]
