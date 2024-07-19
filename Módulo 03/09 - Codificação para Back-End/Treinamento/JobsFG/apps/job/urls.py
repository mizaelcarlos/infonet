from django.urls import path
from .views import *

urlpatterns = [
    path("", VerIndex, name="pg_inicial"),
    path("criar-vaga", CriarVaga, name="pg_criar_vaga"),
    path("criar-empresa", CriarEmpresa, name="pg_criar_empresa"),
    path("detalhes-vaga/<int:id_vaga>", VerDetalhes, name="pg_detalhes")
]
