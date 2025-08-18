from django.db import models
 
class Materia (models.Model):
    nombre=models.CharField()  
    anio=models.CharField()

    def __str__ (self):
        return self.nombre


# Create your models here.
