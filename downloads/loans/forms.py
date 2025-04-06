from django.forms import ModelForm
from .models import LoanApplication
from django import forms
from django.core.exceptions import ValidationError

class LoanApplicationForm(ModelForm):
    class Meta:
        model = LoanApplication
        fields = [
            'dni',
            'cuil',
            'first_name',
            'last_name',
            'email',
            'gender',
            'amount'
        ]
        labels = {
            'dni': 'DNI',
            'cuil': 'CUIL',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'gender': 'Género',
            'amount': 'Monto Solicitado (AR$)',
        }


class LoanApplicationUpdateForm(ModelForm):
    """
    Formulario para la actualizacion de una aplicacion realizada por el admin
    Se agrega el field is_approved, pudiendo asi el administrador aprobar manualmente una aplicacion
    """
    class Meta:
        model = LoanApplication
        fields = [
            'dni',
            'cuil',
            'first_name',
            'last_name',
            'email',
            'gender',
            'amount',
            'is_approved',
        ]
        labels = {
            'dni': 'DNI',
            'cuil': 'CUIL',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'gender': 'Género',
            'amount': 'Monto Solicitado (AR$)',
            'is_approved':'Aprobar aplicacion',
        }
        
"""
https://docs.djangoproject.com/en/5.1/topics/forms/
"""