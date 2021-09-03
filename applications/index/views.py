from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import datetime
from .forms import *
from .models import PublicacionesPlantas, Planta, User
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
    context_object_name = 'ListaPublicaciones'
    paginate_by = 9

    def get_queryset(self):
        busqueda = self.request.GET.get('keyword', '')
        return PublicacionesPlantas.objects.listarPublicacion(busqueda)


class NewPublicacionView(CreateView):
    template_name = 'pub/NuevaPublicacion.html'
    form_class = NewPublicacionForm
    success_url = reverse_lazy('Index_App:Index')

    def NuevaPublicacionRequest(self):
        Plantas = Planta.objects.all()
        return Plantas

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['Plantas'] = self.NuevaPublicacionRequest()
        return data

    def form_valid(self, form):
        user = User.objects.filter(username=self.request.user)
        user = user.get()
        PublicacionesPlantas.objects.create(
            fotografia_Pub=form.cleaned_data['fotografia_Pub'],
            planta_Pub=form.cleaned_data['planta_Pub'],
            lugar_Sembrada_Pub=form.cleaned_data['lugar_Sembrada_Pub'],
            fecha_Sembrada=form.cleaned_data['fecha_Sembrada'],
            sombra=form.cleaned_data['sombra'],
            sol=form.cleaned_data['sol'],
            cuidados=form.cleaned_data['cuidados'],
            usuario=user,
        )
        return super(NewPublicacionView, self).form_valid(form)
