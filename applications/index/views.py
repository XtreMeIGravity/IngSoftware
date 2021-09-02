from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    TemplateView,
)
from .forms import *
from .models import *


# Create your views here.

class IndexView(TemplateView):
    """vista que carga la pagina de inicio"""
    template_name = "Index.html"


class NewPublicacionView(TemplateView):
    template_name = 'pub/NuevaPublicacion.html'
    form_class = NewPublicacionForm
    success_url = '/'

    def form_valid(self, form):
        PublicacionesPlantas.objects.createPublicacion(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            sexo=form.cleaned_data['sexo'],
            fecha_nacimiento=date
        )
        return super(NewPublicacionView, self).form_valid(form)
