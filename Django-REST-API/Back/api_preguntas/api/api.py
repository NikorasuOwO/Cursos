from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from api_preguntas.models import Materia, Tema, Pregunta
from api_preguntas.api.serializers import MateriaSerializer, TemaSerializer, PreguntaSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view

class MateriaAPIView(APIView):

    def get(self, request):

        materias = Materia.objects.all()
        materia_serializador = MateriaSerializer(materias, many=True) # many = true si la consulta evuelve una lista
        return Response(materia_serializador.data)


class TemaAPIView(APIView):

    def get(self, request, materia):

        id_tema = get_object_or_404(Materia, nombre=materia)

        temas = Tema.objects.filter(materia__exact=id_tema)
        tema_serializador = TemaSerializer(temas, many=True) # many = true si la consulta evuelve una lista
        return Response(tema_serializador.data)


"""
class PreguntaAPIView(APIView):

    def get(self, request, tema):  #, format=None, *args, **kwargs
        id_tema = get_object_or_404(Tema, nombre=tema)

        preguntas = Pregunta.objects.filter(tema__exact=id_tema)
        pregunta_serializador = PreguntaSerializer(preguntas, many=True) # many = true si la consulta evuelve una lista
        return Response(pregunta_serializador.data)
"""
@api_view(['GET', 'POST'])
def pregunta_api_view(request, tema):

    if request.method == 'GET':

        id_tema = get_object_or_404(Tema, nombre=tema)

        preguntas = Pregunta.objects.filter(tema__exact=id_tema)
        pregunta_serializador = PreguntaSerializer(preguntas, many=True) # many = true si la consulta evuelve una lista
        return Response(pregunta_serializador.data)

    elif request.method == 'POST':

        pregunta_serializador = PreguntaSerializer(data = request.data) # many = true si la consulta evuelve una lista
        if pregunta_serializador.is_valid():
            pregunta_serializador.save()
            return Response(pregunta_serializador.data)
        return Response(pregunta_serializador.errors)

        

