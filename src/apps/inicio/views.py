from django.views.generic import render, TemplateView

class Pagina_de_inicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context ["titulo"] = "Bienvenido/a"
        context ["mensaje"] = "Esta es la pagina de inicio"
        return context
