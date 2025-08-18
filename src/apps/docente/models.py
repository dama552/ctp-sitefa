from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    fecha_Nacimiento = models.DateField()
    
    def __str__(self):
        return {self.nombre}, {self.apellido}
