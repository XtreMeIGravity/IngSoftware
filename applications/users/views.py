from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
# Create your views here.
from django.views.generic.edit import (
    View,
    FormView,
)

from applications.users.forms import UserRegisterForm, LoginForm
from .models import User


class UserRegisterView(FormView):
    template_name = 'users/registrarUsuario.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        date = form.cleaned_data['fecha_nacimiento']
        print(date)
        date = datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')
        print(date)
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            sexo=form.cleaned_data['sexo'],
            fecha_nacimiento=date
        )
        return super(UserRegisterView, self).form_valid(form)


class LoginUserView(FormView):
    template_name = 'users/loginUsuario.html'
    form_class = LoginForm
    success_url = reverse_lazy('Index_App:Index')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUserView, self).form_valid(form)


class LogOutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'Index_App:Index'
            )
        )


