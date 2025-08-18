from django.db import models

class Horario(models.Model):
    materia = models.CharField(max_length=100)
    dia_semana = models.CharField(max_length=100) #agregar choice
    hora_inicio = models.CharField(max_length=100)
    hora_fin = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.materia}, {self.dia_semana}"
# Create your models here.
