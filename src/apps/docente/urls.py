from django.urls import path
from apps.docente.views import DocenteActualizarVista, DocenteCrearVista, DocenteEliminarVista, DocenteLeerVista

app_name = 'docente'
urlpatterns = [
    path ('crear/', DocenteCrearVista.as_view(), name = 'crear-docente'),
    path ('leer/', DocenteLeerVista.as_view(), name = 'list-docente'),
    path ('actualizar/<int:pk>/', DocenteActualizarVista.as_view(), name = 'actualizar-docente'),
    path ('eliminar/<int:pk>/', DocenteEliminarVista.as_view(), name = 'eliminar-docente'),
]