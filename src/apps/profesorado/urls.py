from django.urls import path
from .views import ProfesoradoLeerVista, ProfesoradoCrearVista, ProfesoradoActualizarVista, ProfesoradoBorrarVista

app_name = "profesorado"

urlpatterns = [
#Profesorado
    path('profesorado/crear/', ProfesoradoCrearVista.as_view(), name = 'profesorado_crear'),
    path('profesorado/creer/', ProfesoradoLeerVista.as_view(), name = 'profesorado_leer'),
    path('profesorado/<int:pk>/editar/', ProfesoradoActualizarVista.as_view(), name = 'profesorado_actualizar'),
    path('profesorado/<int:pk>/eliminar/', ProfesoradoBorrarVista.as_view(), name = 'profesorado_borrar')
]