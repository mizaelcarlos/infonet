from .models import *
from django import forms

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class FormularioEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = "__all__"

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class FormularioServico(forms.ModelForm):
    class Meta:
        model = Servico
        fields = "__all__"

class FormularioOrdemServico(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = "__all__"

class FormularioProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
