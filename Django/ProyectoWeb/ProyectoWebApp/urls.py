
#URLs de la aplicación
from django.urls import path
from ProyectoWebApp import views # Importamos el archivo con las views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # URLs para todo el proyecto
    path('', views.home, name="Home"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
