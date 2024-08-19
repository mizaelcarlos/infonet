from django.shortcuts import render, redirect
from .models import *
from .forms import *
import requests
from django.http import JsonResponse
from django.http import HttpResponse



def VerIndex(request):
    busca_os = OrdemServico.objects.all()

    for os in busca_os:
        valor_os = 0
        for servico in os.servico.all():
            valor_os += servico.valor_servico
        os.valor_total = valor_os

    return render(request, "index.html", {'ordemservicos': busca_os})

# def CriarCliente(request):
#     busca_clientes = Cliente.objects.all()
    
#     if request.method == "GET":
#         novo_cliente = FormularioCliente()
#     else:
#         cliente_preenchido = FormularioCliente(request.POST, request.FILES)
#         if cliente_preenchido.is_valid():
#             cliente_preenchido.save()
#             return redirect("pg_criar_cliente")
#     return render(request, "form-cliente.html", {"form_cliente": novo_cliente, "clientes": busca_clientes})

def CriarCliente(request):
    url = 'http://127.0.0.1:9000/api/clientes' # Substitua pela URL da API real

    obter_token = RetornaToken(request)
    conteudo_bytes = obter_token.content  # Obtém o conteúdo como bytes
    token = conteudo_bytes.decode('utf-8') 

    # Cabeçalhos que você deseja enviar com a solicitação
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'multipart/form-data'
    }
    
    if request.method == "GET":
        novo_cliente = FormularioCliente()

        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
            dados = resposta.json() # Obtém os dados JSON da resposta
        except requests.RequestException as e:
            return HttpResponse(f'Erro ao consumir a API: {str(e)}', status=500)
    
        # Extraia a string desejada do JSON
        clientes = dados['clientes']
        return render(request, "form-cliente.html", {"form_cliente": novo_cliente, "clientes": clientes})
    else:
       # Dados que você deseja enviar no corpo da solicitação POST
        foto = request.FILES.get('foto')

        data = {
            'nome': request.POST['nome'],
            'data_nascimento': request.POST['data_nascimento']
        }

        files = {'foto': (foto.name, foto, foto.content_type)}

               
        # Fazendo a solicitação POST
        response = requests.post(url, data=data,files=files, headers=headers)

        # Obtendo o conteúdo da resposta
        
        if response.status_code in [200, 201]:
            try:
                return redirect("pg_criar_cliente")
            except requests.JSONDecodeError:
                print("A resposta não é um JSON válido.")
        else:
            return HttpResponse(response)
        
def EditarCliente(request, id_cliente):
    busca_cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "GET":
        editar_cliente = FormularioCliente(instance=busca_cliente)
    else:
        cliente_editado = FormularioCliente(request.POST, instance=busca_cliente)
        if cliente_editado.is_valid():
            cliente_editado.save()
            return redirect("pg_criar_cliente")
    return render(request, "form-cliente.html", {"form_cliente": editar_cliente})

def ExcluirCliente(request, id_cliente):
    busca_cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        busca_cliente.delete()
        return redirect("pg_criar_cliente")
    titulo_objeto = busca_cliente.nome
    return render(request, "conf-excluir.html", {"valor": titulo_objeto})

# def CriarEmpresa(request):
#     busca_empresas = Empresa.objects.all()
    
#     if request.method == "GET":
#         nova_empresa = FormularioEmpresa()
#     else:
#         empresa_preenchida = FormularioEmpresa(request.POST)
#         if empresa_preenchida.is_valid():
#             empresa_preenchida.save()
#             return redirect("pg_criar_empresa")
#     return render(request, "form-empresa.html", {"form_empresa": nova_empresa, "empresas": busca_empresas})

def EditarEmpresa(request, id_empresa):
    busca_empresa = Empresa.objects.get(id=id_empresa)
    if request.method == "GET":
        editar_empresa = FormularioEmpresa(instance=busca_empresa)
    else:
        empresa_editada = FormularioEmpresa(request.POST, instance=busca_empresa)
        if empresa_editada.is_valid():
            empresa_editada.save()
            return redirect("pg_criar_empresa")
    return render(request, "form-empresa.html", {"form_empresa": editar_empresa})

def ExcluirEmpresa(request, id_empresa):
    busca_empresa = Empresa.objects.get(id=id_empresa)
    if request.method == "POST":
        busca_empresa.delete()
        return redirect("pg_criar_empresa")
    titulo_objeto = busca_empresa.razao_social
    return render(request, "conf-excluir.html", {"valor": titulo_objeto})

def CriarServico(request):
    busca_servicos = Servico.objects.all()
    
    if request.method == "GET":
        novo_servico = FormularioServico()
    else:
        servico_preenchido = FormularioServico(request.POST)
        if servico_preenchido.is_valid():
            servico_preenchido.save()
            return redirect("pg_criar_servico")
    return render(request, "form-servico.html", {"form_servico": novo_servico, "servicos": busca_servicos})

def EditarServico(request, id_servico):
    busca_servico = Servico.objects.get(id=id_servico)
    if request.method == "GET":
        editar_servico = FormularioServico(instance=busca_servico)
    else:
        servico_editado = FormularioServico(request.POST, instance=busca_servico)
        if servico_editado.is_valid():
            servico_editado.save()
            return redirect("pg_criar_servico")
    return render(request, "form-servico.html", {"form_servico": editar_servico})

def ExcluirServico(request, id_servico):
    busca_servico = Servico.objects.get(id=id_servico)
    if request.method == "POST":
        busca_servico.delete()
        return redirect("pg_criar_servico")
    titulo_objeto = busca_servico.tipo_servico
    return render(request, "conf-excluir.html", {"valor": titulo_objeto})

# def CriarCategoria(request):
#     busca_categorias = Categoria.objects.all()
    
#     if request.method == "GET":
#         nova_categoria = FormularioCategoria()
#     else:
#         categoria_preenchida = FormularioCategoria(request.POST)
#         if categoria_preenchida.is_valid():
#             categoria_preenchida.save()
#             return redirect("pg_criar_categoria")
#     return render(request, "form-categoria.html", {"form_categoria": nova_categoria, "categorias": busca_categorias})

def EditarCategoria(request, id_categoria):
    busca_categoria = Categoria.objects.get(id=id_categoria)
    if request.method == "GET":
        editar_categoria = FormularioCategoria(instance=busca_categoria)
    else:
        categoria_editada = FormularioCategoria(request.POST, instance=busca_categoria)
        if categoria_editada.is_valid():
            categoria_editada.save()
            return redirect("pg_criar_categoria")
    return render(request, "form-categoria.html", {"form_categoria": editar_categoria})

# def ExcluirCategoria(request, id_categoria):
#     busca_categoria = Categoria.objects.get(id=id_categoria)
#     if request.method == "POST":
#         busca_categoria.delete()
#         return redirect("pg_criar_categoria")
#     titulo_objeto = busca_categoria.tipo
#     return render(request, "conf-excluir.html", {"valor": titulo_objeto})

def CriarOrdemServico(request):
    if request.method == "GET":
        nova_ordemservico = FormularioOrdemServico()
    else:
        ordemservico_preenchida = FormularioOrdemServico(request.POST)
        if ordemservico_preenchida.is_valid():
            ordemservico_preenchida.save()
            return redirect("pg_inicial")
    return render(request, "form-ordemservico.html", {"form_ordemservico": nova_ordemservico})

def ExcluirOrdemServico(request, id_os):
    busca_os = OrdemServico.objects.get(id=id_os)
    if request.method == "POST":
        busca_os.delete()
        return redirect("pg_inicial")
    titulo_objeto = "OS: " + str(busca_os.id) + " | " + busca_os.cliente.nome
    return render(request, "conf-excluir.html", {"valor": titulo_objeto})

def CriarProduto(request):
    busca_produtos = Produto.objects.all()
    
    if request.method == "GET":
        novo_produto = FormularioProduto()
    else:
        produto_preenchido = FormularioProduto(request.POST, request.FILES)
        if produto_preenchido.is_valid():
            produto_preenchido.save()
            return redirect("pg_criar_produto")
    return render(request, "form-produto.html", {"form_produto": novo_produto, "produtos": busca_produtos})

def EditarProduto(request, id_produto):
    busca_produto = Produto.objects.get(id=id_produto)
    if request.method == "GET":
        editar_produto = FormularioProduto(instance=busca_produto)
    else:
        produto_editado = FormularioProduto(request.POST, instance=busca_produto)
        if produto_editado.is_valid():
            produto_editado.save()
            return redirect("pg_criar_produto")
    return render(request, "form-produto.html", {"form_produto": editar_produto})

def ExcluirProduto(request, id_produto):
    busca_produto = Produto.objects.get(id=id_produto)
    if request.method == "POST":
        busca_produto.delete()
        return redirect("pg_criar_produto")
    titulo_objeto = busca_produto.nome
    return render(request, "conf-excluir.html", {"valor": titulo_objeto})

def ibge(request):
    api = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios"
    requisicao = requests.get(api)

    try:
        municipios = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    lista_municipios = []
    for  municipio in municipios:
        lista_municipios.append(municipio)

    return render(request, "ibge.html", {"municipios": lista_municipios, "requisicao" : requisicao})

def RetornaToken(request):
    url = 'http://127.0.0.1:9000/api/login' # Substitua pela URL da API real
    try:
        # Dados que você deseja enviar no corpo da solicitação POST
        json = {
            'email': 'mizaelcarlos4455@gmail.com',
            'password' : 'Maziel2941*@'
        }
        # Cabeçalhos que você deseja enviar com a solicitação
        headers = {
            'Content-Type': 'application/json'
        }

        # Fazendo a solicitação POST
        request = requests.post(url, json=json, headers=headers)
        response = request.json()
    except requests.RequestException as e:
        return HttpResponse(f'Erro ao consumir a API: {str(e)}', status=500)
    
    return HttpResponse(response['token'], content_type="text/plain")


def CriarCategoria(request):
    url = 'http://127.0.0.1:9000/api/categorias' # Substitua pela URL da API real

    obter_token = RetornaToken(request)
    conteudo_bytes = obter_token.content  # Obtém o conteúdo como bytes
    token = conteudo_bytes.decode('utf-8') 

    # Cabeçalhos que você deseja enviar com a solicitação
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    
    if request.method == "GET":
        nova_categoria = FormularioCategoria()

        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
            dados = resposta.json() # Obtém os dados JSON da resposta
        except requests.RequestException as e:
            return HttpResponse(f'Erro ao consumir a API: {str(e)}', status=500)
    
        # Extraia a string desejada do JSON
        categorias = dados['categorias']
        return render(request, "form-categoria.html", {"form_categoria": nova_categoria, "categorias": categorias})
    else:
       # Dados que você deseja enviar no corpo da solicitação POST
        json = {
            'tipo': request.POST['tipo']
        }
               
        # Fazendo a solicitação POST
        response = requests.post(url, json=json, headers=headers)

        # Obtendo o conteúdo da resposta
        
        if response.status_code in [200, 201]:
            try:
                response_data = response.json()
                return redirect("pg_criar_categoria")
            except requests.JSONDecodeError:
                print("A resposta não é um JSON válido.")
        else:
            return HttpResponse('Erro ao consumir a API: ', response.status_code)
    
def ExcluirCategoria(request, id_categoria):
    url = 'http://127.0.0.1:9000/api/categorias/' + str(id_categoria) # Substitua pela URL da API real

    obter_token = RetornaToken(request)
    conteudo_bytes = obter_token.content  # Obtém o conteúdo como bytes
    token = conteudo_bytes.decode('utf-8') 

    # Cabeçalhos que você deseja enviar com a solicitação
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    
    if request.method == "GET":             
        # Fazendo a solicitação DELETE
        response = requests.delete(url, headers=headers)

        # Obtendo o conteúdo da resposta
        
        if response.status_code in [200]:
            try:
                return redirect("pg_criar_categoria")
            except requests.JSONDecodeError:
                print("A resposta não é um JSON válido.")
        else:
            return HttpResponse('Erro ao consumir a API: ', response.status_code)

def CriarServico(request):
    url = 'http://127.0.0.1:9000/api/servicos' # Substitua pela URL da API real
    url_categorias = 'http://127.0.0.1:9000/api/categorias'
    url_empresas = 'http://127.0.0.1:9000/api/empresas'

    obter_token = RetornaToken(request)
    conteudo_bytes = obter_token.content  # Obtém o conteúdo como bytes
    token = conteudo_bytes.decode('utf-8') 

    # Cabeçalhos que você deseja enviar com a solicitação
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    resposta_categorias = requests.get(url_categorias, headers=headers)
    resposta_categorias.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
    dados_categorias = resposta_categorias.json() # Obtém os dados JSON da resposta
    categorias = dados_categorias['categorias']

    resposta_empresas = requests.get(url_empresas, headers=headers)
    resposta_empresas.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
    dados_empresas = resposta_empresas.json() # Obtém os dados JSON da resposta
    empresas = dados_empresas['empresas']
    
    if request.method == "GET":
        novo_servico = FormularioServico()

        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
            dados = resposta.json() # Obtém os dados JSON da resposta
        except requests.RequestException as e:
            return HttpResponse(f'Erro ao consumir a API: {str(e)}', status=500)
    
        # Extraia a string desejada do JSON
        servicos = dados['servicos']
        return render(request, "form-servico.html", {"categorias": categorias,"empresas": empresas, "servicos": servicos})
    else:
       # Dados que você deseja enviar no corpo da solicitação POST
        json = {
            'tipo': request.POST['tipo'],
            'valor': request.POST['valor'],
            'empresa_id': request.POST['empresa_id'],
            'categoria_id': request.POST['categoria_id'],
        }
               
        # Fazendo a solicitação POST
        response = requests.post(url, json=json, headers=headers)

        # Obtendo o conteúdo da resposta
        
        if response.status_code in [200, 201]:
            try:
                response_data = response.json()
                return redirect("pg_criar_servico")
            except requests.JSONDecodeError:
                print("A resposta não é um JSON válido.")
        else:
            return HttpResponse('Erro ao consumir a API: ', response.status_code)
        
def ExcluirServico(request, id_servico):
    url = 'http://127.0.0.1:9000/api/servicos/' + str(id_servico) # Substitua pela URL da API real

    obter_token = RetornaToken(request)
    conteudo_bytes = obter_token.content  # Obtém o conteúdo como bytes
    token = conteudo_bytes.decode('utf-8') 

    # Cabeçalhos que você deseja enviar com a solicitação
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    if request.method == "GET":             
        # Fazendo a solicitação DELETE
        response = requests.delete(url, headers=headers)

        # Obtendo o conteúdo da resposta
        
        if response.status_code in [200]:
            try:
                return redirect("pg_criar_servico")
            except requests.JSONDecodeError:
                print("A resposta não é um JSON válido.")
        else:
            return HttpResponse('Erro ao consumir a API: ', response.status_code)
        
def EditarCategoria(request, id_categoria):
    url_editar_categoria = 'http://127.0.0.1:9000/api/categorias/' + str(id_categoria) # Substitua pela URL da API real
    url_listar_categorias = 'http://127.0.0.1:9000/api/categorias' # Substitua pela URL da API real

    obter_token = RetornaToken(request)
    conteudo_bytes = obter_token.content  # Obtém o conteúdo como bytes
    token = conteudo_bytes.decode('utf-8') 

    # Cabeçalhos que você deseja enviar com a solicitação
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    resposta = requests.get(url_editar_categoria, headers=headers)
    resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
    dados = resposta.json()
    categoria = dados['categoria']

    resposta_categorias = requests.get(url_listar_categorias, headers=headers)
    resposta_categorias.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
    dados_categorias = resposta_categorias.json() # Obtém os dados JSON da resposta
    categorias = dados_categorias['categorias']

    if request.method == "GET":
        return render(request, "form-categoria.html", {"categoria": categoria, 'categorias' : categorias}) 
    else:
        # Dados que você deseja enviar no corpo da solicitação POST
        json = {
            'tipo': request.POST['tipo']
        }
               
        # Fazendo a solicitação POST
        response = requests.put(url_editar_categoria, json=json, headers=headers)

        # Obtendo o conteúdo da resposta
        
        if response.status_code in [200, 201]:
            try:
                return redirect("pg_criar_categoria")
            except requests.JSONDecodeError:
                print("A resposta não é um JSON válido.")
        else:
            return render(request, "form-categoria.html", {"categoria": categoria, 'categorias' : categorias}) 


def CriarEmpresa(request):

    url = 'http://127.0.0.1:9000/api/empresas' # Substitua pela URL da API real

    obter_token = RetornaToken(request)
    conteudo_bytes = obter_token.content  # Obtém o conteúdo como bytes
    token = conteudo_bytes.decode('utf-8') 

    # Cabeçalhos que você deseja enviar com a solicitação
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    
    if request.method == "GET":
        novo_empresa = FormularioEmpresa()

        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
            dados = resposta.json() # Obtém os dados JSON da resposta
        except requests.RequestException as e:
            return HttpResponse(f'Erro ao consumir a API: {str(e)}', status=500)
    
        # Extraia a string desejada do JSON
        empresas = dados['empresas']
        return render(request, "form-empresa.html", {"form_empresa": novo_empresa, "empresas": empresas})
    else:
       # Dados que você deseja enviar no corpo da solicitação POST
        json = {
            'razaoSocial': request.POST['razao_social'],
            'cnpj': request.POST['cnpj']
        }
               
        # Fazendo a solicitação POST
        response = requests.post(url, json=json, headers=headers)

        # Obtendo o conteúdo da resposta
        
        if response.status_code in [200, 201]:
            try:
                response_data = response.json()
                return redirect("pg_criar_empresa")
            except requests.JSONDecodeError:
                print("A resposta não é um JSON válido.")
        else:
            return HttpResponse('Erro ao consumir a API: ', response.status_code)