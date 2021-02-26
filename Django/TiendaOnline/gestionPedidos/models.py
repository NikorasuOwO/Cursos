from django.db import models

# Create your models here.

class Cliente(models.Model): # Hereda de model
    nombre = models.CharField(max_length=30) # Campo String de 30 caracteres
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    tfno = models.CharField(max_length=7)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30, default='articulo')
    seccion = models.CharField(max_length=20, default='seccion')
    precio = models.IntegerField(default=0)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateTimeField()
    entregado = models.BooleanField()
