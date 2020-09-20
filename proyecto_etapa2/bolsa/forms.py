from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ("titulo", "descripcion","imagen","categoria","fecha_caducacion")


    #def __init__(self,variables_extras, *args, **kwargs):
    #super(OfertaForm, self).__init__(*args, **kwargs)
    #self.fields["categoria"].queryset = Categoria.objects.filter(titulo__icontains = "" )