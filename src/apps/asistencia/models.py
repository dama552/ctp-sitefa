from django.db import models

class Asistencia (models.Model):
    fecha =  models.DateField()
    
    
    def __str__(self):
          return self.fecha
    

# Create your models here.