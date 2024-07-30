Para utilizar o método DELETE de um controller e poder remover registros do model Produto basta usar o código a seguir:

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

Para consumir esse método DELETE no Postman basta, seguir conforme a imagem abaixo:

![image](https://github.com/user-attachments/assets/5c3c2418-109c-4b12-b8f9-9d45f642edfa)

Para utilizar o método PUT e permitir atualizar registros do model Produto, basta usar o código a seguir:

<pre class="language-php">
  <code class="language-php">
    public function update(Request $request, $id)
    {
        $produto = Produto::find($id);
        if (!$produto) {
            return response()->json(['message' => 'Produto não encontrado'], 404);
        }

        $validator = Validator::make($request->all(), [
            'nome' => 'string|max:255',
            'valor' => 'integer',
        ]);

        if ($validator->fails()) {
            return response()->json(['errors' => $validator->errors()], 422);
        }

        $produto->update($request->all());

        return response()->json([
            'status' => true,
            'message' => "Produto atualizado com sucesso!",
            'produto' => $produto
        ], 200);
    }
  </code>
</pre>
