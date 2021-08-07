from django.db.models import fields
from api_preguntas.models import Materia, Tema, Pregunta
from rest_framework import serializers

class MateriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materia
        fields = ['nombre']

class TemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tema
        fields = ['nombre']

class PreguntaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregunta
        fields = '__all__'