from django.shortcuts import render
from apps.docente.models import Docente
from .models import Docente
from django.views import generic
from django.urls import reverse_lazy

#Docente
class DocenteCrearVista(generic.CreateView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/crear.html'
    success_urls = reverse_lazy ('docente:list-docente')
    
class DocenteActualizarVista(generic.UpdateView):
    model = Docente
    fields = '__all__'
    template_name = 'Docente/actualizar.html'
    success_urls = reverse_lazy ('docente:list-docente')
    
    
class DocenteEliminarVista(generic.DeleteView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/eliminar.html'
    success_urls = reverse_lazy ('docente:list-docente')
    
class DocenteListaVista(generic.ListView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/Lista.html'
    success_urls = reverse_lazy ('docente:list-docente')
    context_object_name='docentes'
