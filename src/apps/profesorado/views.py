from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from models import Profesorado

# Create your views here.
class ProfesoradoLeerVista(ListView):
    model = Profesorado
    template_name = 'profesorado/leer.html'
    context_object_name = 'profesorados'

class ProfesoradoCrearVista(CreateView):
    model = Profesorado
    fields = '__all__'
    template_name = 'profesorado/crear.html'
    success_url = reverse_lazy('profesorado:profesorado_list')

class ProfesoradoActualizarVista(UpdateView):
    model = Profesorado
    fields = '__all__'
    template_name = 'profesorado/actualizar.html'
    success_url = reverse_lazy('profesorado:profesorado_list')

class ProfesoradoBorrarVista(DeleteView):
    model = Profesorado
    template_name = 'profesorado/borrar.html'
    success_url = reverse_lazy('profesorado:profesorado_list')