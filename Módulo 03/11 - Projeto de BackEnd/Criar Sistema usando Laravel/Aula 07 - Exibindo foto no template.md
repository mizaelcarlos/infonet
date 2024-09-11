## Antes de tudo deverá ser resolvido a qustão do upload da foto, vou mostrar abaixo o exemplo de um formulaário:


        <h1>Editar Contato</h1>
        ### <form action="{{ route('contato.update',$contato->id) }}" method="post" enctype="multipart/form-data">
            @csrf
            @method('PUT')
            <label for="">Email: </label>
            <input type="text" name="email" id="email" value="{{ $contato->email }}">
            <label for="">Telefone</label>
            <input type="text" name="telefone" id="telefone" value="{{$contato->telefone  }}">
            <label>Foto</label>
            <input type="file" name="foto" id="foto" >
            ### <img src="{{  asset('storage/' . $contato->foto) }}" alt="" width="100" height="100">
            <button type="submit">Salvar</button>
        </form>



### Após isso implemente o upload da foto no método do controller que pode ser o store ou update

<pre class="language-php">
  <code class="language-php">
     public function store(Request $request)
      {
          $request->validate([
              'email' => 'required',
              'telefone' => 'required',
          ]);
  
          $foto_camimho = $request->file('foto')->store('fotos', 'public');
  
          // Criar o cliente com o caminho da foto
          $contato = Contato::create([
              'email' => $request->email,
              'telefone' => $request->telefone,
              'foto' => $foto_camimho,
          ]);
  
  
          return redirect()->route('contato.index');
      }
  </code>
</pre>


### Primeiro rode o comando abaixo para criar um link simbólico para pasta storage

<pre class="language-php">
  <code class="language-php">
    php artisan storage:link
  </code>
</pre>

Após isso recupere a foto no seu template usando a tag img passando o valor abaixo para o src conforme abaixo:


### src="{{  asset('storage/' . $contato->foto) }}"

