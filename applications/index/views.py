from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
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
from django.views.generic.edit import (
    View,
    FormView,
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


class UserPubView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('Users_App:user-login')

    template_name = 'pub/UserListPub.html'
    context_object_name = 'ListaPublicaciones'
    paginate_by = 9

    def get_queryset(self):
        busqueda = self.request.GET.get('keyword', '')
        return PublicacionesPlantas.objects.listarPublicacionByUser(self.request.user, busqueda)


class NewPublicacionView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('Users_App:user-login')

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
        """user = User.objects.filter(username=self.request.user)
        user = user.get()"""
        PublicacionesPlantas.objects.createPublicacion(
            fotografia_Pub=form.cleaned_data['fotografia_Pub'],
            planta_Pub=form.cleaned_data['planta_Pub'],
            lugar_Sembrada_Pub=form.cleaned_data['lugar_Sembrada_Pub'],
            fecha_Sembrada=form.cleaned_data['fecha_Sembrada'],
            sombra=form.cleaned_data['sombra'],
            sol=form.cleaned_data['sol'],
            cuidados=form.cleaned_data['cuidados'],
            usuario=self.request.user
        )
        return super(NewPublicacionView, self).form_valid(form)


# update view
class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('Users_App:user-login')
    model = PublicacionesPlantas
    template_name = "pub/ActualizarPublicacion.html"
    """form_class = NewPublicacionForm"""
    """funciona"""
    form_class = UpdatePublicacionForm
    success_url = reverse_lazy('Index_App:user-publicaciones')

    def __init__(self, *args, **kwargs):
        super(PublicacionUpdateView, self).__init__(*args, **kwargs)  # This is not working

    # Intercept values of POST
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Logic Process
        empleado = form.save()
        empleado.save()
        return super(PublicacionUpdateView, self).form_valid(form)


# delete view
class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = PublicacionesPlantas
    context_object_name = 'PublicacionAEliminar'
    template_name = "pub/DeletePublicacion.html"
    success_url = reverse_lazy('Index_App:user-publicaciones')
