from django.contrib import admin
from .models import Estudiante 

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'apellido', 'profesor']
    search_fields = ['nombre']
    list_filter = ['edad']
    ordering = ['nombre']

# Register your models here.
