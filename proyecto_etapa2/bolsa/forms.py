from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    fecha_caducacion=forms.DateField(widget=forms.TextInput(attrs={"placeholder":"01/01/1000"}))

    class Meta:
        model = Oferta
        fields = ("titulo", "descripcion","imagen","fecha_caducacion")

