from django import forms
from .models import Fruta

class FrutaForm(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = ['nombre', 'precio', 'cantidad']