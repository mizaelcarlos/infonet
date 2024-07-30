No Arquivo ProdutoController.php implemente o seguinte método:

<pre class="language-php">
  <code class="language-php">
   public function show($id)
    {
        $produto = Produto::find($id);

        if (!$produto) {
            return response()->json(['message' => 'Produto não encontrado'], 404);
        }
        
        return response()->json([
            'status' => true,
            'produto' => $produto
        ]);
    }
  </code>
</pre>

Após isso , basta inserir a rota no arquivo web.php 

<pre class="language-php">
  <code class="language-php">
    Route::get('/produtos/{id}', [ProdutoController::class, 'show']);
  </code>
</pre>

Para testar o método basta usar o postman conforme a imagem abaixo:

![image](https://github.com/user-attachments/assets/714fc7e3-16fb-4a74-b5a2-a14b245ef243)


