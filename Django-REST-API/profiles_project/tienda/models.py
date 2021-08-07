from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=200)
    stock = models.IntegerField(default=100)
    precio = models.FloatField()

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
    
    def __str__(self):
        return self.nombre