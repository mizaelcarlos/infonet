from django.shortcuts import render, redirect
from .models import *
from .forms import *

def ListaGeral(request):
    busca_abencoados = Abencoado.objects.all()
    busca_tacas = Taca.objects.all()
    return render(request, "index.html", {"abencoados": busca_abencoados, "tacas": busca_tacas})

def CriarAbencoado(request):
    if request.method == "POST":
        novo_abencoado = FormularioAbencoado(request.POST)
        if novo_abencoado.is_valid():
            novo_abencoado.save()
            return redirect("pg_inicial")
    else:
        novo_abencoado = FormularioAbencoado()
    return render(request, "new-abencoado.html", {"formulario": novo_abencoado})