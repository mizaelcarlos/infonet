No arquivo urls.py insira a rota abaixo:

<pre class="language-php">
  <code class="language-php">
      path("token", RetornaToken, name="token"),
  </code>
</pre>



No arquivo views.py insira os métodos abaixo:

<pre class="language-php">
  <code class="language-php">
      from django.shortcuts import render, redirect
      from .models import *
      from .forms import *
      import requests
      from django.http import JsonResponse
      from django.http import HttpResponse

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
    
    Código pra o template form-servico.html

  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <link rel="stylesheet" href="{% static "style-formularios.css" %}">
          <title>Formulário Serviço</title>
      </head>
      <body>
          <a href="{% url "pg_inicial" %}">
              <button>Voltar</button>
          </a>
  
          <a href="{% url "pg_criar_categoria" %}">
              <button>+ Categoria</button>
          </a>
  
          <h2>Formulário Serviço</h2>
  
          <form method="post">
              {% csrf_token %}
              <p>
              <label for="tipo">Tipo servico:</label>
              <input type="text" name="tipo" maxlength="100" required="" id="tipo">
              </p>
                  
                  
              <p>
              <label for="valor">Valor servico:</label>
              <input type="number" name="valor" step="0.01" required="" id="valor">
              </p>
                  
                  
              <p>
              <label for="id_empresa">Empresa:</label>
              <select name="empresa_id" required="" id="empresa_id">
                  <option value="" selected=""></option>
                  {% for empresa in empresas %}
                      <option value="{{ empresa.id }}">{{ empresa.razaoSocial }}</option>
                  {% endfor %}
              </select>
              </p>
                  
                  
              <p>
              <label for="id_categoria">Categoria:</label>
              <select name="categoria_id" required="" id="categoria_id">
                  <option value="" selected=""></option>
                  {% for categoria in categorias %}
                      <option value="{{ categoria.id }}">{{ categoria.tipo }}</option>
                  {% endfor %}
              </select>
              </p>
              <button type="submit">Salvar</button>
              <a href="{% url "pg_inicial" %}">
                  <button type="button">Cancelar</button>
              </a>
          </form>    
  
          <h2>Lista de Serviços</h2>
  
          {% for servico in servicos %}
              <div class="card-formulario">
                  <span>{{ servico.tipo }}</span>
                  <span>R$ {{ servico.valor }}</span>
                  <span><b>Empresa:</b> {{ servico.empresa.razaoSocial }}</span>
                  <span><b>Categoria:</b> {{ servico.categoria.tipo }}</span>
                  <div class="btns_formulario">
                      <a href="{% url "pg_editar_servico" servico.id %}">
                          <span>Editar Serviço</span>
                      </a>
                      <a href="{% url "pg_excluir_servico" servico.id %}">
                          <span>Excluir Serviço</span>
                      </a>
                  </div>
              </div>
          {% endfor %}
  
      </body>
  </html>

  </code>
</pre>
