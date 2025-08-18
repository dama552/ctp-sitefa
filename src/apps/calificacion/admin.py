from django.contrib import admin
from .models import Calificacion
# Register your models here.
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
	list_display = ('numero',)
	search_fields = ('numero',)
	list_filter = ('numero',)
	ordering = ('numero',)