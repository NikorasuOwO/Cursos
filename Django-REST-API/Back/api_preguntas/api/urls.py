from django.urls import path
from api_preguntas.api.api import MateriaAPIView, TemaAPIView #, PreguntaAPIView
from api_preguntas.api.api import pregunta_api_view

urlpatterns = [
    path('preguntastema/<str:tema>/', pregunta_api_view, name='todo-preguntasXtema'), # DEVUELVE PREGUNTAS DEL TEMA
    path('temasmateria/<str:materia>/', TemaAPIView.as_view(), name='todo-temasXmateria'),
    path('materias/', MateriaAPIView.as_view(), name='todo materias'), # DEVUELVE TODAS LAS MATERIAS
    


]
