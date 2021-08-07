from django.contrib import admin
from .models import Producto

# Register your models here.

#class producto_admin(admin.ModelAdmin):

admin.site.register(Producto)
