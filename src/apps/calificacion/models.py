from django.db import models

#Crea tus modelos aquí.
class Calificacion(models.Model):
    numero= models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return f"{self.numero}"
