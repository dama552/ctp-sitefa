from django.db import models
 
class Materia (models.Model):
    nombre=models.Charfield(max_lenght=100)  
    def __str__ (self):
        return f"{self.nombre}"

# Create your models here.
