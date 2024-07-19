from django import forms
from .models import *

class FormularioAbencoado(forms.ModelForm):
    class Meta:
        model = Abencoado
        fields = '__all__'

class FormularioTaca(forms.ModelForm):
    class Meta:
        model = Taca
        fields = '__all__'
