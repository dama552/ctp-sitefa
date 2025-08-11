from django.db import models

class Estudiante (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)
    
    def __str__(self):
          return self.nombre
    

# Create your models here.