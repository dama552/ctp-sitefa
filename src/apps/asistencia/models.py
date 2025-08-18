from django.db import models

from apps.estudiante.models import Estudiante
from apps.materia.models import Materia

class Asistencia (models.Model):
    fecha =  models.CharField(max_length=100)
    presente = models.BooleanField(default=False)
    justificación = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE,related_name="estudiante")
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE,related_name="asistencia")
    
    def __str__(self):
          return self.fecha
     

# Create your models here.