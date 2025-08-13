from django.contrib import admin
from .models import Materia
# Register your models here.
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    search_fields = ("nombre")
    list_filter = ("nombre")
    ordering = ("nombre")
