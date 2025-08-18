from django.db import models

#Crea tus modelos aquí.
class Calificacion(models.Model):
    numero= models.DecimalField(max_digits=5, decimal_places=2)
    materia =  models.CharField(max_length=100)
    estudiante = models.CharField(max_length=100)
    nota = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    # Agrega más campos según sea necesario
