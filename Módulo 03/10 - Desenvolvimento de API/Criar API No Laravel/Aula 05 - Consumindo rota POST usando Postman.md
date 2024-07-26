
Rodar comando a baixo no terminal, para gerar a chave da aplicação

<pre class="language-php">
  <code class="language-php">
   php artisan key:generate
  </code>
</pre>

![image](https://github.com/user-attachments/assets/12c18027-781a-4116-8d0e-b2069ffb7060)


Para poder acessar e consumir as rotas geradas pela API , basta acessar o cmd ou terminal na pasta do projeto e iniciar o servidor usando o comando abaixo:


<pre class="language-php">
  <code class="language-php">
  php artisan serve
  </code>
</pre>

Será mostrado conforma a imagem abaixo:

![image](https://github.com/user-attachments/assets/8e6e1f33-46a2-4f25-8bcd-623de63eef88)

a url para poder consumir ou executar o projeto é o seguinte:

http://127.0.0.1:8000/

Agora vamos usar a ferramenta Postman para testar a API

Primeiro deverá ser gerado o token , usando a rota:

<pre class="language-php">
  <code class="language-php">
    http://127.0.0.1:8000/token
  </code>
</pre>

Ao clicar em enviar , será gerar o token:

![image](https://github.com/user-attachments/assets/e3980b1b-17fd-45af-a35c-65fde9bd748c)

Copiar o token mostrado no resultado

Caso eu queira consumir a rota que trás a listagem de todos os produtos , basta usar conforme a imagem abaixo:

<pre class="language-php">
  <code class="language-php">
   http://127.0.0.1:8000/produtos
  </code>
</pre>


![image](https://github.com/user-attachments/assets/2d1be8fc-11ae-4770-ba64-9f2e821fa952)

deverá ser inserido os parametros de cabeçalho na opção HEADERS

- Accept : application/json
- X-CSRF-TOKEN : colar token aqui

Na opção Params, passar os parametros do produto a ser cadastrado na API:

![image](https://github.com/user-attachments/assets/715d6995-75f2-4a12-aacf-ee29dc3f7603)


Ao clicar em Send (enviar) ,será mostrado no body do resultado na parte de baixo da tela, um JSON retornando o produto cadastrado na API, EXEMPLO.

<pre class="language-php">
  <code class="language-php">
  {
    "status": true,
    "message": "Produto Criado com sucesso!",
    "produto": {
        "nome": "Notebook",
        "valor": "100",
        "descricao": "LG",
        "updated_at": "2024-07-26T12:27:30.000000Z",
        "created_at": "2024-07-26T12:27:30.000000Z",
        "id": 7
    }
}
  </code>
</pre>







