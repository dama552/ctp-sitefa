from django.db import models

class Estudiante(models.Model):
	nombre = models.CharField(max_length=100)
	profesor = models.CharField(max_length=100)
	edad = models.IntegerField()

	def __str__(self):
		return self.nombre