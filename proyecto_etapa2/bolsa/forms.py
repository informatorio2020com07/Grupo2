from django import forms
from .models import Oferta,Categoria

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ("oferente", "titulo", "descripcion", "categoria",)
    def __init__(self, *args, **kwargs):
        super(OfertaForm, self).__init__(*args, **kwargs)
        self.fields["oferente"].widget.attrs.update({'class' : '','placeholder': '', 'type': ''})
        self.fields["titulo"].widget.attrs.update({'class' : 'validate','placeholder' : 'titulo de la oferta', 'type' : 'text'})
        self.fields["descripcion"].widget.attrs.update({'class' : 'materialize-textarea','placeholder' : 'Descripcion ', 'type' : 'text'})
        self.fields["categoria"].widget.attrs.update({'class' : '','placeholder' : '', 'type' : ''})        


class OcategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ("nombre_cat","descripcion","titulo")