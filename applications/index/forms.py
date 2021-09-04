from django import forms
from django.forms import ValidationError
import time
from .models import PublicacionesPlantas, User


def validateDateEs(date):
    """        Funcion para validar una fecha en formato        """
    try:
        result = time.strptime(date, '%d/%m/%Y')
        return True
    except:
        pass
    return False


class NewPublicacionForm(forms.ModelForm):
    fotografia_Pub = forms.ImageField(
        label="Fotografia",
        required=True,
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Fecha de Sembrado',
                'class': 'form-control form-control-sm'
            }
        )
    )
    fecha_Sembrada = forms.CharField(
        label="Fecha de sembrado",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Fecha de Sembrado',
                'class': 'form-control form-control-sm'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(NewPublicacionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not (visible.field.label == 'Sol' or visible.field.label == 'Sombra'):
                visible.field.widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        """meta definition for userForm"""
        model = PublicacionesPlantas
        fields = ['planta_Pub', 'fotografia_Pub', 'lugar_Sembrada_Pub', 'fecha_Sembrada', 'sombra', 'sol', 'cuidados']
        widgets = {
            'fecha_Sembrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%d-%m-%Y'),
        }


class UpdatePublicacionForm(forms.ModelForm):
    fotografia_Pub = forms.ImageField(
        label="Fotografia",
        required=True,
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Fecha de Sembrado',
                'class': 'form-control form-control-sm'
            }
        )
    )
    fecha_Sembrada = forms.CharField(
        label="Fecha de sembrado",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Fecha de Sembrado',
                'class': 'form-control form-control-sm'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(UpdatePublicacionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not (visible.field.label == 'Sol' or visible.field.label == 'Sombra'):
                visible.field.widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        """meta definition for userForm"""
        model = PublicacionesPlantas
        fields = ['planta_Pub', 'fotografia_Pub', 'lugar_Sembrada_Pub', 'fecha_Sembrada', 'sombra', 'sol', 'cuidados']
        widgets = {
            'fecha_Sembrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%d-%m-%Y'),
        }
