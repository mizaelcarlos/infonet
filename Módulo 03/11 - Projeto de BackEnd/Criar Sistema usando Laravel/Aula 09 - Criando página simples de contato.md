### Criar primeiro o controller chamado de ContatoController

### Após isso criar o método index dentro do  ContatoController.php

<pre class="language-php">
  <code class="language-php">
      public function index(){
        return view('contato.index');
      }
  </code>
</pre>

### Após isso crie a rota do arquivo routes/web.php

<pre class="language-php">
  <code class="language-php">
      Route::get('/contato',[ContatoController::class, 'index'])->name('contato.index');
  </code>
</pre>

### Após isso crie o template na pasta contato/index.blade.php com o conteúdo abaixo


    <form action="" method="post">
        <label for="">Nome</label>
        <input type="text" name="nome" id="nome">
        <label for="">Email</label>
        <input type="text" name="email" id="email">
        <label for="">Mensagem</label>
        <textarea name="mensagem" id="" cols="30" rows="10"></textarea>
    </form>


### Após isso basta colocar a rota num botão ou link para poder ser acessada, conforme o exemplo abaixo:

```markdown
  <a href="{{ route('mensagem.index') }}">Contato</a>







