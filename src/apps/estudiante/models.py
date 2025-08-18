from django.db import models

class Estudiante(models.Model):
	nombre=models.CharField(max_length=200)
	dni = models.IntegerField()
	email = models.CharField(max_length=70)
	telefono = models.IntegerField()
	direccion = models.CharField(maxlength=100)
	fecha_nacimiento = models.DateField(null=True)
	carrera = models.CharField(max_length=60)
	ciclo_ingreso = models.CharField(max_length=40)
	estados = {
		"REGULAR": "Regular",
		"IRREGULAR": "Irregular",
		"OTRO": "Otro"
	}
	estado = models.CharField(max_length=50, choices=estados)
	materias_inscriptas = models.CharField(max_length=300)

	
	def __str__ (self):
		return f"{self.nombre},{self.apellido}"