from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Materia


class MateriaLeerVista(ListView):
    model = Materia
    template_name = 'materia/leer.html'
    context_object_name = 'materias'
    paginate_by = 10  # opcional

    def get_queryset(self):
        queryset = super().get_queryset()
        selected_anio = self.request.GET.get('anio')

        if selected_anio:
            queryset = queryset.filter(anio=selected_anio)

        return queryset.order_by('anio', 'nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anios = Materia.objects.values_list('anio', flat=True).distinct().order_by('anio')
        context['anios'] = anios
        context['selected_anio'] = self.request.GET.get('anio', '')
        return context


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
    template_name = 'materia/eliminar.html'
    success_url = reverse_lazy('materia:materia_leer')
