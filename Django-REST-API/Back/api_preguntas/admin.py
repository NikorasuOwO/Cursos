from django.contrib import admin
from .models import Pregunta, Materia, Tema

# Register your models here.

class MateriaAdmin(admin.ModelAdmin):
    fields = ('nombre',)

class TemaAdmin(admin.ModelAdmin):
    fields = ('nombre', 'materia',)

class PreguntaAdmin(admin.ModelAdmin):
    fields = ('tema', ('content', 'h5p'))

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)