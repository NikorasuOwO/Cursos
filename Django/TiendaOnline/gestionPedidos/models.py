from django.db import models

# Create your models here.

class Clientes(models.Model): # Hereda de model
    nombre = models.CharField(max_length=30) # Campo String de 30 caracteres
    direccion = models.CharField(max_length=50, verbose_name="La dirección")
    email = models.EmailField(blank=True, null=True)
    tfno = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Articulos(models.Model):
    nombre = models.CharField(max_length=30, default='articulo')
    seccion = models.CharField(max_length=20, default='seccion')
    precio = models.IntegerField(default=0)

    def __str__(self):
        return 'nombre: %s seccion: %s precio: %s' %(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateTimeField()
    entregado = models.BooleanField()
