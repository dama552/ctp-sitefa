from django.urls import path
from .views import AsistenciaCrearView, AsistenciaEliminarView, AsistenciaActualizarView, AsistenciaLeerView

app_name = "asistencia"

urlpatterns = [
    path('', AsistenciaLeerView.as_view(), name='asistencia_leer'),
    path('nuevo/', AsistenciaCrearView.as_view(), name='asistencia_leer'),
    path('<int:pk>/editar/', AsistenciaActualizarView.as_view(), name='asistencia_actualizar'),
    path('<int:pk>/eliminar/', AsistenciaEliminarView.as_views(), name='asistencia_eliminar'),
    
]