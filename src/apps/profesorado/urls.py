from django.urls import path
from .views import ProfesoradoLeerVista, ProfesoradoCrearVista, ProfesoradoActualizarVista, ProfesoradoBorrarVista

app_name = "profesorado"

#Profesorado
urlpatterns = [
    path('leer/', ProfesoradoLeerVista.as_view(), name = 'profesorado_leer'),
    path('crear/', ProfesoradoCrearVista.as_view(), name = 'profesorado_crear'),
    path('actualizar/<int:pk>', ProfesoradoActualizarVista.as_view(), name = 'profesorado_actualizar'),
    path('eliminar/<int:pk>', ProfesoradoBorrarVista.as_view(), name = 'profesorado_eliminar')
]