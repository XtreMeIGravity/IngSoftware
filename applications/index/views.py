from django.shortcuts import render

# Create your views here.

from .forms import *
from .models import *


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

# Create your views here.

# GRID DATA
class IndexView(ListView):
    template_name = 'Index.html'
    model = PublicacionesPlantas
    context_object_name = 'ListaPublicaciones'
    paginate_by = 7

    def get_queryset(self):
        busqueda = self.request.GET.get('keyword', '')
        lista = PublicacionesPlantas.objects.filter(
            planta_Pub__nombre_Planta__icontains=busqueda,
        )
        return lista


class NewPublicacionView(TemplateView):
    template_name = 'pub/NuevaPublicacion.html'
    form_class = NewPublicacionForm
    success_url = '/'

    def form_valid(self, form):
        PublicacionesPlantas.objects.createPublicacion()
        return super(NewPublicacionView, self).form_valid(form)
