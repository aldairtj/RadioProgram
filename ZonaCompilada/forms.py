from django import forms # type: ignore
from .models import Oyente

class FormularioOyente(forms.ModelForm):
    class Meta:
        model = Oyente
        fields = ['nombre', 'apellidos', 'correo', 'telefono']
