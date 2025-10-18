# src/apps/calificacion/forms.py
from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'materia', 'nota', 'comentario']