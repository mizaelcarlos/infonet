### Antes de tudo deverá ser colocado a coluna status do tipo boolean na tabela de cliente.
## Caso não tenha feito isso, crie uma migration com a nova coluna e rode o comando para aplicar a migration
## Após isso insira a coluna status nos campos prenchiveis do Model/Cliente.php

## Após isso crie o método a ser acionado no ClienteController.php, conforme exemplo abaixo:

<pre class="language-php">
  <code class="language-php">
     public function atualizarStatus(Request $request,$id){
        $contato = Contato::find($id);
        $contato->status = true;
        $contato->save();

        return redirect()->route('contato.index');

    }
  </code>
</pre>

## Após isso crie a rota para acionar o método criado no controlador, a rota sempre no arquivo routes/web.php

<pre class="language-php">
  <code class="language-php">
      Route::post('/contato/{id}/ativar', [ContatoController::class, 'atualizarStatus'])->name('contato.atualizarStatus');
  </code>
</pre>

## Após isso nas opções da listagem de clientes , insira a opção para ativar/inativar o cliente usando um icone pra ação do formulário abaixo:
## Essa ação ficará abaixo da opção de excluir:


      <form action="{{ route('contato.atualizarStatus', $contato->id) }}" method="POST" style="display:inline;">
        @csrf
        @method('POST')
        <button type="submit">Ativar</button>
    </form>

