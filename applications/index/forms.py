from django import forms
from django.forms import ValidationError
import time
from .models import PublicacionesPlantas


class NewPublicacionForm(forms.ModelForm):
    """Form definition users"""
    fecha_Sembrada = forms.CharField(
        label="Fecha de sembrado",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Fecha de nacimiento',
                'class': 'form-control form-control-sm'
            }
        )
    )

    class Meta:
        """meta definition for userForm"""
        model = PublicacionesPlantas
        fields = ('fotografia_Pub',
                  'planta_Pub',
                  'lugar_Sembrada_Pub',
                  'fecha_Sembrada',
                  'sombra',
                  'sol',
                  'cuidados',
                  )
        widgets = {
            'cuidados': forms.Textarea(),
            'habilidades': forms.ChoiceField(),
        }

    def validateDateEs(self, date):
        """        Funcion para validar una fecha en formato        """
        try:
            result = time.strptime(date, '%d/%m/%Y')
            return True
        except:
            pass
        return False

    def clean_fecha_Sembrada(self):
        date = self.cleaned_data['fecha_Sembrada']
        if not self.validateDateEs(date):
            raise ValidationError('Fecha no valida')
        return date
