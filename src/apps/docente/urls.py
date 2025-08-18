from django.urls import path
from apps.docente.views import DocenteActualizarVista, DocenteCrearVista, DocenteEliminarVista, DocenteListaVista

app_name = 'docente'
urlpatterns = [
    path ('docente/crear/', DocenteCrearVista.as_view(), name = 'crear-docente'),
    path ('docente/lista/', DocenteListaVista.as_view(), name = 'list-docente'),
    path ('docente/<int:pk>/editar/', DocenteActualizarVista.as_view(), name = 'actualizar-docente'),
    path ('docente/<int:pk>/eliminar/', DocenteEliminarVista.as_view(), name = 'eliminar-docente'),
]