from django import forms
from .models import *

class FormularioEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = "__all__"

class FormularioVaga(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = "__all__"