from django.db import models
from apps.Materia.models import Materia
from apps.Estudiante.models import Estudiante

from apps.estudiante.models import Estudiante
from apps.materia.models import Materia

#Crea tus modelos aquí.
class Calificacion(models.Model):
    numero= models.DecimalField(max_digits=5, decimal_places=2)
    nota = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='calificacion')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='calificacion')

    # Agrega más campos según sea necesario
