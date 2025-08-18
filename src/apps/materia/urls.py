from django.urls import path
from views import MateriaCrearVista,MateriaActualizarVista,MateriaEliminarVista,MateriaLeerVista

app_name = 'materia'

urlpatterns = [
    path("materia/leer/",MateriaLeerVista.as_view(),name="materia_leer"),
    path("materi/crear/",MateriaCrearVista.as_view(),name="materia_crear"),
    path("materia/<int:pk>/actualizar/",MateriaActualizarVista.as_view(),name="materia_actualizar"),
    path("materia/<int:pk>/eliminar/",MateriaEliminarVista.as_view(),name="materia_eliminar")
]