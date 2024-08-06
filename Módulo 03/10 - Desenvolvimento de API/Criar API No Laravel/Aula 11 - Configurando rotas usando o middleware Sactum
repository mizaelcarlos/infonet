Certifique-se de que o guard de autenticação do Sanctum está configurado corretamente no arquivo config/auth.php. O guard sanctum deve estar definido:


<pre class="language-php">
  <code class="language-php">
      'guards' => [
          'web' => [
              'driver' => 'session',
              'provider' => 'users',
          ],
      
          'api' => [
              'driver' => 'sanctum',
              'provider' => 'users',
              'hash' => false,
          ],
      ],
  </code>
</pre>

Após issso , limpe o cache das configurações, das rotas e da aplicação:

<pre class="language-php">
  <code class="language-php">
      php artisan config:cache
      php artisan route:cache
      php artisan cache:clear
  </code>
</pre>
