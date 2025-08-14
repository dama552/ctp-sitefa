from django.contrib import admin
from .models import Horario

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_filter = ['nombre']
    ordering = ['nombre']


# Register your models here.

