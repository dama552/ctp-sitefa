from django.db import models
 
class Materia (models.Model):
    nombre=models.CharField()
    nombre=models.CharField()  
    anio=models.CharField()
    profesorado=models.ForeignKey(Profesorado,on_delete=models.CASCADE,related_name="materia")

    def __str__ (self):
        return self.nombre


# Create your models here.
