from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion",)

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "tfno") # Campos que vamos a enseñar
    search_fields = ("nombre", "tfno") # Campos posibles de búsqueda

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
