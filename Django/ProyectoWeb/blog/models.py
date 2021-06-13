from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):

    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True) # Puede ser opcional

    autor = models.ForeignKey(User, on_delete=models.CASCADE) # Cada post va asociado con un usuario
                                                            # Si se borra el usuario se borran los posts asociados
    categorias = models.ManyToManyField(Categoria) # Relación de varios a varios con catergorias

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo
