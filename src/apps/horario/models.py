from django.db import models

class Horario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

# Create your models here.
