from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    imagen=forms.ImageField(required=False)
    class Meta:
        model = Oferta
        fields = ("titulo", "descripcion","imagen","fecha_caducacion")

class SearchForm(forms.Form):
    titulo = forms.CharField(max_length=30, required = False)
    
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs["placeholder"] = "Ingrese profesion"
        