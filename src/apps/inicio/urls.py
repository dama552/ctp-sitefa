from django.urls import path 
from .views import Pagina_de_inicio

urlpatterns = [
    path("", Pagina_de_inicio.as_view(), name="inicio"),
]