### Para Editar e excluir é necessário implementar os métodos, edit, update, destroy no controller:

<pre class="language-php">
  <code class="language-php">

    namespace App\Http\Controllers;
    
    use App\Models\Contato;
    use Illuminate\Http\Request;
    
    class ContatoController extends Controller
    {
        /**
         * Display a listing of the resource.
         */
        public function index()
        {
            $contatos = Contato::all();
    
            return view('contato.index', ['contatos' => $contatos]);
        }
    
        /**
         * Show the form for creating a new resource.
         */
        public function create()
        {
            return view('contato.cadastrar');
        }
    
        /**
         * Store a newly created resource in storage.
         */
        public function store(Request $request)
        {
            $request->validate([
                'email' => 'required',
                'telefone' => 'required',
            ]);
    
            Contato::create($request->all());
    
            return redirect()->route('contato.index');
        }
    
        /**
         * Display the specified resource.
         */
        public function show(Contato $contato)
        {
            //
        }
    
        /**
         * Show the form for editing the specified resource.
         */
        public function edit($id)
        {
            $contato = Contato::find($id);
            return view('contato.editar', ['contato' => $contato]);
        }
    
        /**
         * Update the specified resource in storage.
         */
        public function update(Request $request, $id)
        {
            $contato = Contato::find($id);
            $contato->update($request->all());
    
            return redirect()->route('contato.index')->with('success', 'Contato atualizado com sucesso.');
    
        }
    
        /**
         * Remove the specified resource from storage.
         */
        public function destroy($id)
        {
            $contato = Contato::find($id);
            $contato->delete();
            return redirect()->route('contato.index')->with('success', 'Contato excluído com sucesso.');
    
        }
    }
  </code>
</pre>
### Após isso configure as rotas no arquivo routes/web.php 

<pre class="language-php">
  <code class="language-php">
    Route::get('/contato', [ContatoController::class, 'index'])->name('contato.index');
    Route::get('/contato/cadastrar', [ContatoController::class, 'create'])->name('contato.create');
    Route::get('/contato/editar/{id}', [ContatoController::class, 'edit'])->name('contato.edit');
    Route::post('/contato', [ContatoController::class, 'store'])->name('contato.salvar');
    Route::delete('/contato/{id}', [ContatoController::class, 'destroy'])->name('contato.destroy');
    Route::put('/contato/{id}', [ContatoController::class, 'update'])->name('contato.update');
    Route::get('/contato/{id}', [ContatoController::class, 'show'])->name('contato.show');
  </code>
</pre>

### Após isso editar o arquivo resource/contato/index.blade.php , conforme abaixo:


    <h2>Lista de Contatos</h2>

    <table class="table">
        <thead>
            <tr>
            <th scope="col">ID</th>
            <th scope="col">EMAIL</th>
            <th scope="col">TELEFONE</th>
            <th scope="col">OPÇÕES</th>
            </tr>
        </thead>
        <tbody>
            @foreach($contatos as $contato)
                <tr>
                    <th scope="row">{{ $contato->id }}</th>
                    <td>{{ $contato->email }}</td>
                    <td>{{ $contato->telefone }}</td>
                    <td>
                        <div class="btns_formulario">
                            <a href="{{ route('contato.edit', $contato->id) }}">
                                <span>Editar</span>
                            </a>
                            <form action="{{ route('contato.destroy', $contato->id) }}" method="POST" style="display:inline;">
                                @csrf
                                @method('DELETE')
                                <button type="submit">Excluir</button>
                            </form>
                        </div>
                    </td>
                </tr>
                @endforeach
        </tbody>
    </table>


### Em seguida crie o arquivo resource/contato/editar.blade.php e insira esse formulário nele:


    <form action="{{ route('contato.update',$contato->id) }}" method="post">
        @csrf
        @method('PUT')
        <label for="">Email: </label>
        <input type="text" name="email" id="email" value="{{ $contato->email }}">
        <label for="">Telefone</label>
        <input type="text" name="telefone" id="telefone" value="{{$contato->telefone  }}">
        <button type="submit">Salvar</button>
    </form>




