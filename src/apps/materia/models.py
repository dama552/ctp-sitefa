from django.db import models
 
class Materia (models.Model):
    nombre=models.CharField()  
    def __str__ (self):
        return f"{self.nombre}"

# Create your models here.
