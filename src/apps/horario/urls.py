from django.urls import path
from .views import HorarioCrearVista, HorarioLeerVista, HorarioActualizarVista, HorarioEliminarVista

app_name = 'horario'

urlpatterns = [
    path('horario/crear/',HorarioCrearVista.as_view( ), name='horario_crear'),
    path('horario/leer/',HorarioLeerVista.as_view( ), name='horario_leer'),
    path('horario/<int:pk>/actualizar/',HorarioActualizarVista.as_view( ), name='horario_actualizar'),
    path('horario/<int:pk>/eliminar/',HorarioEliminarVista.as_view( ), name='horario_eliminar')
]