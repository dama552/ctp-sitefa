from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Calificacion

class CalificacionListView(ListView):
    model = Calificacion
    template_name = 'calificacion/leer.html'
    context_object_name = 'calificacion' # Esta es la variable que


class CalificacionCreateView(CreateView):
    model = Calificacion
    fields = '__all__'
    template_name = 'calificacion/crear.html'
    success_url = reverse_lazy('Calificacion:calificacion_leer')


class CalificacionUpdateView(UpdateView):
    model = Calificacion
    fields = '__all__'
    template_name = 'calificacion/actualizar.html'
    success_url = reverse_lazy('Calificacion:calificacion_leer')

class CalificacionDeleteView(DeleteView):
    model = Calificacion
    template_name = 'calificacion/eliminar.html'
    success_url = reverse_lazy('Calificacion:calificacion_leer')