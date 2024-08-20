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

Inserir rotas no arquivo routes/api.php
<pre class="language-php">
  <code class="language-php">
       
  
  Route::middleware('auth:sanctum')->group(function(){
      Route::get('/produtos', [ProdutoController::class, 'index']);
      Route::post('/produtos', [ProdutoController::class, 'store']);
      Route::delete('/produtos/{id}', [ProdutoController::class, 'destroy']);
      Route::put('/produtos/{id}', [ProdutoController::class, 'update']);
      Route::get('/produtos/{id}', [ProdutoController::class, 'show']);
    
      Route::get('/categorias', [CategoriaController::class, 'index']);
      Route::post('/categorias', [CategoriaController::class, 'store']);
      Route::delete('/categorias/{id}', [CategoriaController::class, 'destroy']);
      Route::put('/categorias/{id}', [CategoriaController::class, 'update']);
      Route::get('/categorias/{id}', [CategoriaController::class, 'show']);

      Route::get('/empresas', [EmpresaController::class, 'index']);
      Route::post('/empresas', [EmpresaController::class, 'store']);
      Route::delete('/empresas/{id}', [EmpresaController::class, 'destroy']);
      Route::put('/empresas/{id}', [EmpresaController::class, 'update']);
      Route::get('/empresas/{id}', [EmpresaController::class, 'show']);

      Route::get('/servicos', [ServicoController::class, 'index']);
      Route::post('/servicos', [ServicoController::class, 'store']);
      Route::delete('/servicos/{id}', [ServicoController::class, 'destroy']);
      Route::put('/servicos/{id}', [ServicoController::class, 'update']);
      Route::get('/servicos/{id}', [ServicoController::class, 'show']);

      Route::get('/clientes', [ClienteController::class, 'index']);
      Route::post('/clientes', [ClienteController::class, 'store']);
      Route::delete('/clientes/{id}', [ClienteController::class, 'destroy']);
      Route::put('/clientes/{id}', [ClienteController::class, 'update']);
      Route::get('/clientes/{id}', [ClienteController::class, 'show']);

      Route::get('/ordemServicos', [OrdemServicoController::class, 'index']);
      Route::post('/ordemServicos', [OrdemServicoController::class, 'store']);
      Route::delete('/{id}', [OrdemServicoController::class, 'destroy']);
      Route::put('/{id}', [OrdemServicoController::class, 'update']);
      Route::get('/{id}', [OrdemServicoController::class, 'show']);
  });  

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
