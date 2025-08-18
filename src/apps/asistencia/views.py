from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Asistencia


class AsistenciaLeerView(ListView):
    model =  Asistencia
    template_name = 'asistencia/leer.html'
    context_object_name = 'asistencia'

class AsistenciaCrearView(CreateView):
    model = Asistencia
    fields = '__all__'
    template_name = 'asistencia/crear.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')

class AsistenciaActualizarView(UpdateView):
    model = Asistencia
    fields = '__all__'
    template_name = 'asistencia/actualizar.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')
    
class AsistenciaEliminarView(DeleteView):
    model = Asistencia
    template_name = 'asistencia/eliminar.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')