Comece criando um novo projeto Laravel usando composer:

Onde sistema_os será o nome do projeto 

<pre class="language-php">
  <code class="language-php">
  composer create-project laravel/laravel sistema_os
  </code>
</pre>




Para iniciar o servidor, execute o seguinte comando, que roda o servidor de aplicativos na porta 8000:

<pre class="language-php">
  <code class="language-php">
  cd sistema_os
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
    DB_DATABASE=sistema_os
    DB_USERNAME=root
    DB_PASSWORD=
  </code>
</pre>


lembrando que as configurações acima estão relacionadas ao SGBD MYSQL





