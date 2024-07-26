
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


Caso eu queira consumir a rota que trás a listagem de todos os produtos , basta usar conforme a imagem abaixo:

<pre class="language-php">
  <code class="language-php">
   http://127.0.0.1:8000/produtos
  </code>
</pre>


![image](https://github.com/user-attachments/assets/ed771ba1-3f21-4611-8269-ecb70fc5e620)

Ao clicar em Send (enviar) ,será mostrado no body do resultado na parte de baixo da tela, um JSON retornando todos os produtos cadastrados no sistema, EXEMPLO.

<pre class="language-php">
  <code class="language-php">
   {
    "status": true,
    "produtos": [
        {
            "id": 1,
            "nome": "teste",
            "valor": 50,
            "descricao": "teste",
            "created_at": "2024-07-25T14:24:46.000000Z",
            "updated_at": "2024-07-25T14:24:46.000000Z"
        } ]
  }
  </code>
</pre>







