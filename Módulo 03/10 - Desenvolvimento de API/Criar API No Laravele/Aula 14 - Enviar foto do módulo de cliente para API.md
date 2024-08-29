## Alterar template com formulário de cadastro de cliente, inserindo apenas o enctype="multipart/form-data"


     <form method="post" id='form_cliente' enctype="multipart/form-data">
        {% csrf_token %}
        <p>
            <label for="id_cliente">Nome:</label>
            <input type="text" name="nome" maxlength="100"  id="nome" value="{{ cliente.nome}}">  
        </p>
        <p>
            <label for="id_cliente">Data de Nascimento:</label>
            <input type="date" name="data_nascimento" maxlength="100"  id="data_nascimento" value="{{ cliente.data_nascimento}}">  
        </p>
        <p>
            <label for="id_cliente">Foto:</label>
            <input type="file" name="foto">
        </p>       
        <p>
            <img src="{{ foto }}"> 
        </p>
        <!--<button type="submit">Enviar</button>-->
        <button type="submit"class='btn btn-primary'>Salvar</button>
        <a href="{% url "pg_criar_cliente" %}">
            <button type="button"class='btn btn-danger'>Cancelar</button>
        </a>
      </form>  

## A única parte que foi adicionada foi o trecho abaixo:

<pre class="language-php">
  <code class="language-php">
  foto = request.FILES.get('foto')
   files = {
            'foto': (foto.name, foto, foto.content_type)
        }
   response = requests.post(url, data=data, files=files, headers=headers)

  </code>
</pre>


## No arquivo de views.py o método def CriarCliente ficará assim:

<pre class="language-php">
  <code class="language-php">
     def CriarCliente(request):
    url = 'http://127.0.0.1:9000/api/clientes'  # Substitua pela URL da API real

    obter_token = RetornaToken(request)
    conteudo_bytes = obter_token.content  # Obtém o conteúdo como bytes
    token = conteudo_bytes.decode('utf-8') 

    # Cabeçalhos que você deseja enviar com a solicitação
    headers = {
        'Authorization': 'Bearer ' + token,
        # 'Content-Type': 'application/json'
    }
    
    if request.method == "GET":
        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
            dados = resposta.json()  # Obtém os dados JSON da resposta
        except requests.RequestException as e:
            return HttpResponse(f'Erro ao consumir a API: {str(e)}', status=500)
    
        # Extraia a string desejada do JSON
        clientes = dados['clientes']
        return render(request, "form-cliente.html", { "clientes": clientes })
    else:
        # Dados que você deseja enviar no corpo da solicitação POST
        foto = request.FILES.get('foto')
        nome = request.POST['nome']
        data_nascimento = request.POST['data_nascimento']

        # Preparando os dados para envio
        files = {
            'foto': (foto.name, foto, foto.content_type)
        }
        data = {
            'nome': nome,
            'data_nascimento': data_nascimento
        }
       
        response = requests.post(url, data=data, files=files, headers=headers)

        # return HttpResponse(response)
        
        if response.status_code in [200, 201]:
            try:
                response_data = response.json()
                return redirect("pg_criar_cliente")
            except requests.JSONDecodeError:
                return HttpResponse("A resposta não é um JSON válido.", status=500)
        else:
            return HttpResponse(f'Erro na solicitação: {response.status_code}', status=response.status_code)
  </code>
</pre>

## Já na API Laravel o código  do método store ficará assim:

<pre class="language-php">
  <code class="language-php">
      public function store(Request $request)
      {
          $request->validate([
              'nome' => 'required|string|max:255',
              'data_nascimento' => 'required|date',
              'foto' => 'required|image|mimes:jpeg,png,jpg,gif|max:2048', // Validação da imagem
          ]);
  
          // Armazenar a foto
          $foto_camimho = $request->file('foto')->store('fotos', 'public');
  
          // Criar o cliente com o caminho da foto
          $clientes = Cliente::create([
              'nome' => $request->input('nome'),
              'data_nascimento' => $request->input('data_nascimento'),
              'foto' => $request->file(),
          ]);
  
          return response()->json([
              'status' => true,
              'message' => "Cliente Cadastrado com sucesso!",
              'cliente' => $clientes
          ], 200);
      }
  </code>
</pre>
