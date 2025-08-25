from django.urls import path
from .views import MateriaCrearVista,MateriaActualizarVista,MateriaEliminarVista,MateriaLeerVista

app_name = 'materia'

urlpatterns = [
    path("leer/",MateriaLeerVista.as_view(),name="materia_leer"),
    path("crear/",MateriaCrearVista.as_view(),name="materia_crear"),
    path("actualizar/<int:pk>/",MateriaActualizarVista.as_view(),name="materia_actualizar"),
    path("eliminar/<int:pk>/",MateriaEliminarVista.as_view(),name="materia_eliminar")
]