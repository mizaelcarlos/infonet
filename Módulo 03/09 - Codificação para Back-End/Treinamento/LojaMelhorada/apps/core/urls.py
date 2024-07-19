from django.urls import path
from .views import *

urlpatterns = [
    path('', ListaGeral, name="pg_inicial"),
    path("novo-abencoado", CriarAbencoado, name="pg_new_abencoado")
]
