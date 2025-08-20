from django.urls import path
from .views import EstudianteCrearVista, EstudianteActualizarVista, EstudianteEliminarVista, EstudianteLeerVista
app_name = 'estudiante'

urlpatterns = [ 
    path('estudiante/crear', EstudianteCrearVista.as_view(), name='Estudiante_crear'),
    path('estudiante/eliminar', EstudianteEliminarVista.as_view(), name='Estudiante_eliminar'),
    path('estudiante/leer', EstudianteLeerVista.as_view(), name='Estudiante_leer'),
    path('estudiante/actualizar', EstudianteActualizarVista.as_view(), name='Estudiante_actualizar'),
]