from django.urls import path
from .views import EstudianteCrearVista, EstudianteActualizarVista, EstudianteEliminarVista, EstudianteLeerVista
app_name = 'estudiante'

urlpatterns = [ 
    path('crear/', EstudianteCrearVista.as_view(), name='Estudiante_crear'),
    path('eliminar/<int:pk>', EstudianteEliminarVista.as_view(), name='Estudiante_eliminar'),
    path('leer/', EstudianteLeerVista.as_view(), name='Estudiante_Leer'),
    path('actualizar/<int:pk>', EstudianteActualizarVista.as_view(), name='Estudiante_actualizar'),
]