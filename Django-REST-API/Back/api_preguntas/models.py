from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now

# Create your models here.

class Materia(models.Model):

    nombre = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Tema(models.Model):
    
    nombre = models.CharField(max_length=100)
    materia = models.ForeignKey("Materia", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre + " (%s)" % self.materia

class Pregunta(models.Model):

    content = models.JSONField()
    h5p = models.JSONField()
    tema = models.ForeignKey("api_preguntas.Tema", on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "pregunta de " + str(self.tema)
