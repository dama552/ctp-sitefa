from django.db import models

class Asistencia (models.Model):
    materia = models.CharField(max_length=100)
    fecha =  models.CharField(max_length=100)
    estudiante = models.CharField(max_length=100)
    presente = models.BooleanField(default=False)
    justificación = models.CharField(max_length=100)
    
    def __str__(self):
          return self.fecha
     

# Create your models here.