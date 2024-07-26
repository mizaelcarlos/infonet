Professor - Mizael Carlos

O Laravel Eloquent é uma maneira fácil de interagir com seu banco de dados. É um mapeador objeto-relacional (ORM) que simplifica as complexidades dos bancos de dados, fornecendo um modelo para interagir com as tabelas.

Como tal, o Laravel Eloquent tem excelentes ferramentas para criar e testar APIs para dar suporte ao seu desenvolvimento. Neste artigo prático, você verá como é fácil criar e testar APIs usando o Laravel.

Nesta demonstração, você começará criando um modelo que pode ser usado para criar a API e a tabela do banco de dados. Daí verá como adicionar um controlador como camada de lógica de negócios e uma rota para concluir a API. Em seguida, você aprenderá a realizar testes de APIs usando o Postman antes de finalmente se concentrar na autenticação e no tratamento de erros.

Pré-requisitos , Para começar, eis o que você precisará:

- Laravel ultima versão
- Composer
- Postman
- XAMPP ou Wampserver (Servidor Apache)
- Conhecimento básico de APIs e PHP


Comece criando um novo projeto Laravel usando composer:

<pre class="language-php">
  <code class="language-php">
  composer create-project laravel/laravel laravel-api
  </code>
</pre>




Para iniciar o servidor, execute o seguinte comando, que roda o servidor de aplicativos na porta 8000:

<pre class="language-php">
  <code class="language-php">
  cd laravel-api
  </code>
</pre>

<pre class="language-php">
  <code class="language-php">
  php artisan serve
  </code>
</pre>


Você deverá ver a tela a seguir:

![image](https://github.com/user-attachments/assets/75f6d671-dc91-403a-933d-c7df21b636fb)


para fazer conexão do banco de dados com o projeto , edite as seguinte informações do arquivo .env abaixo:

<pre class="language-php">
  <code class="language-php">
    DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_DATABASE=api
    DB_USERNAME=root
    DB_PASSWORD=
  </code>
</pre>


lembrando que as configurações acima estão relacionadas ao SGBD MYSQL





