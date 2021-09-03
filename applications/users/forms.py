from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
import time
from .models import User


class UserRegisterForm(forms.ModelForm):
    """Form definition users"""

    sexo = forms.ChoiceField(
        required=True,
        choices=User.Gender_Choices,
        initial=0,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-sm'
            }
        )
    )
    fecha_nacimiento = forms.CharField(
        label="Fecha de nacimiento",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Fecha de nacimiento',
                'class': 'form-control form-control-sm'
            }
        )
    )

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'form-control form-control-sm'
            }
        )
    )

    password2 = forms.CharField(
        label='Repetir Contraseña',
        required=True,
        min_length=5,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'form-control form-control-sm'
            }
        )
    )
    username = forms.CharField(
        label='Nombre de usuario',
        required=True,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control form-control-sm'
            }
        )
    )
    email = forms.CharField(
        label='Correo Electronico',
        required=True,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control form-control-sm'
            }
        )
    )
    nombres = forms.CharField(
        label='Nombres',
        required=True,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombres',
                'class': 'form-control form-control-sm'
            }
        )
    )
    apellidos = forms.CharField(
        label='Apellidos',
        required=True,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Apellidos',
                'class': 'form-control form-control-sm'
            }
        )
    )

    class Meta:
        """meta definition for userForm"""
        model = User
        fields = ('username', 'email', 'nombres', 'apellidos', 'sexo')

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')

    def validateDateEs(self, date):
        """
        Funcion para validar una fecha en formato
        """
        try:
            result = time.strptime(date, '%d/%m/%Y')
            return True
        except:
            pass
        return False

    def clean_fecha_nacimiento(self):
        date = self.cleaned_data['fecha_nacimiento']
        if not self.validateDateEs(date):
            raise ValidationError('Fecha no valida')
        return date


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'class': 'form-control form-control-sm'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'form-control form-control-sm'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data
