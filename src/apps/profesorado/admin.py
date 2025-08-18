from django.contrib import admin
from .models import Profesorado

admin.site.register(Profesorado)
# Register your models here.
@admin.register(Profesorado)
class ProfesoradoAdmin(admin.ModelAdmin):
    list_display = ('nombre_instituto','carreras','ciclo_lectivo')
    search_fields = ('nombre_instituto','carreras','ciclo_lectivo')
    list_filter = ('nombre_instituto','carreras','ciclo_lectivo')
    ordering = ('nombre_instituto','carreras','ciclo_lectivo')