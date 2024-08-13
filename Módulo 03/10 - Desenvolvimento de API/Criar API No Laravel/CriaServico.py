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
  
