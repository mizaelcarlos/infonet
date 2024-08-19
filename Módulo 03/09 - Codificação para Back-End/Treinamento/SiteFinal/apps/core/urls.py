from django.urls import path, include
from .views import *

urlpatterns = [
    path("", VerIndex, name="pg_inicial"),
    path("criar-cliente", CriarCliente, name="pg_criar_cliente"),
    path("editar-cliente/<int:id_cliente>", EditarCliente, name="pg_editar_cliente"),
    path("excluir-cliente/<int:id_cliente>", ExcluirCliente, name="pg_excluir_cliente"),
    path("criar-empresa", CriarEmpresa, name="pg_criar_empresa"),
    path("editar-empresa/<int:id_empresa>", EditarEmpresa, name="pg_editar_empresa"),
    path("excluir-empresa/<int:id_empresa>", ExcluirEmpresa, name="pg_excluir_empresa"),
    path("criar-servico", CriarServico, name="pg_criar_servico"),
    path("editar-servico/<int:id_servico>", EditarServico, name="pg_editar_servico"),
    path("excluir-servico/<int:id_servico>", ExcluirServico, name="pg_excluir_servico"),
    path("criar-categoria", CriarCategoria, name="pg_criar_categoria"),
    path("editar-categoria/<int:id_categoria>", EditarCategoria, name="pg_editar_categoria"),
    path("excluir-categoria/<int:id_categoria>", ExcluirCategoria, name="pg_excluir_categoria"),
    path("criar-ordemservico", CriarOrdemServico, name="pg_criar_ordemservico"),
    path("excluir-ordemservico/<int:id_os>", ExcluirOrdemServico, name="pg_excluir_ordemservico"),
    path("criar-produto", CriarProduto, name="pg_criar_produto"),
    path("editar-produto/<int:id_produto>", EditarProduto, name="pg_editar_produto"),
    path("excluir-produto/<int:id_produto>", ExcluirProduto, name="pg_excluir_produto"),





    
    path("ibge", ibge, name="ibge"),
    path("token", RetornaToken, name="token"),

]
