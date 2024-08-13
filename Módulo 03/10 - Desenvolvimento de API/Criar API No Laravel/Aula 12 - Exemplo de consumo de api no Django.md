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

  </code>
</pre>
