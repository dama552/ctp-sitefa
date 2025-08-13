from django.contrib import admin
from .models import Asistencia

# Register your models here.
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('fecha')
    search_fields = ('fecha')
    list_filter = ('fecha')
    ordering = ('fecha')