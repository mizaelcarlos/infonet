Para utilizar o método DELETE de um controller e poder remover registros da tabela produto basta usar o código a seguir:

<pre class="language-php">
  <code class="language-php">
  public function destroy($id)
    {
        $produto = Produto::find($id);
        if (!$produto) {
            return response()->json(['message' => 'Produto não encontrado'], 404);
        }

        $produto->delete();
        return response()->json(['message' => 'Produto removído com sucesso']);
    }
  </code>
</pre>

Após isso , basta configurar no arquivo de rotas web.php a rota para esse método:

<pre class="language-php">
  <code class="language-php">
    Route::delete('/produtos/{id}', [ProdutoController::class, 'destroy']);
  </code>
</pre>
