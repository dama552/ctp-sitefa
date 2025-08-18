from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Materia 
# Create your views here.

class MateriaLeerVista(ListView):
    model = Materia
    template_name = 'materia/leer.html'
    context_object_name = 'materias'
    

class MateriaCrearVista(CreateView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/crear.html'
    success_url = reverse_lazy('materia:materia_leer')
    
class MateriaActualizarVista(UpdateView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/actualizar.html'
    success_url = reverse_lazy('materia:materia_leer')

class MateriaEliminarVista(DeleteView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/eliminar.html'
    success_url = reverse_lazy('materia:materia_leer')
