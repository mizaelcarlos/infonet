### O Laravel Breeze é um pacote que facilita a configuração de autenticação. 

### Para funcionar é preciso instalar o node, use o link abaixo para fazer o download.
https://nodejs.org/pt

### Antes de tudo faça um backup do seu arquivo routes/web.php por que o conteúdo dele será substituído.

#### Instalar o Laravel Breeze:
<pre class="language-php">
  <code class="language-php">
      composer require laravel/breeze --dev
  </code>
</pre>

#### Instalar o Breeze:
<pre class="language-php">
  <code class="language-php">
      php artisan breeze:install
  </code>
</pre>

### Escolher a opção blade, yes e depois 0 

#### Migrar o banco de dados:
<pre class="language-php">
  <code class="language-php">
      php artisan migrate
 </code>
</pre>


#### O Breeze já cria as rotas de autenticação para você. Confira as rotas em routes/web.php. Você verá rotas para registro, login, logout e redefinição de senha.

### Testar a Autenticação
<pre class="language-php">
  <code class="language-php">
      php artisan serve
 </code>
</pre>

#### Visite http://localhost:8000/register para se registrar e http://localhost:8000/login para fazer login.

### Personalização

#### Você pode personalizar a autenticação modificando as views em resources/views/auth e ajustando a lógica em app/Http/Controllers/Auth.

### Protegendo Rotas
<pre class="language-php">
  <code class="language-php">
      Route::middleware(['auth'])->group(function () {
        Route::get('/dashboard', [DashboardController::class, 'index']);
      });
 </code>
</pre>

### Logout 

### O logout pode ser realizado facilmente usando a rota gerada pelo Breeze:

<pre class="language-php">
  <code class="language-php">
      Route::post('/logout', [AuthenticatedSessionController::class, 'destroy'])
      ->name('logout');
 </code>
</pre>

### Após isso , limpe o cache das rotas

### Protegendo Rotas
<pre class="language-php">
  <code class="language-php">
      php artisan route:cache
 </code>
</pre>



