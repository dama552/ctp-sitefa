from django.db import models

# Create your models here.
class Profesorado(models.Model):
    nombre_instituto = models.CharField(max_length=100)
    carreras = models.CharField(max_length=100)
    cilco_lectivo = models.CharField(max_length=100)