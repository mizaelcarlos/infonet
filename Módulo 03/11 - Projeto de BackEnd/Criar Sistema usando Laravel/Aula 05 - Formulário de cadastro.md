Controller:

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
          public function edit(Contato $contato)
          {
              //
          }
      
          /**
           * Update the specified resource in storage.
           */
          public function update(Request $request, Contato $contato)
          {
              //
          }
      
          /**
           * Remove the specified resource from storage.
           */
          public function destroy(Contato $contato)
          {
              //
          }
      }
  </code>
</pre>

Arquivo de rotas localizado na pasta routes/web.php 
<pre class="language-php">
  <code class="language-php">
   Route::get('/contato', [ContatoController::class, 'index'])->name('contato.index');
   Route::get('/contato/cadastrar', [ContatoController::class, 'create'])->name('contato.create');
   Route::post('/contato', [ContatoController::class, 'store'])->name('contato.salvar');
   Route::delete('/contato/{id}', [ContatoController::class, 'destroy'])->name('contato.destroy');
   Route::put('/contato/{id}', [ContatoController::class, 'update'])->name('contato.update');
   Route::get('/contato/{id}', [ContatoController::class, 'show'])->name('contato.show');
  </code>
</pre>

Fomrulario de cadastro  contato/cadastrar.blade.php 


      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Cadastrar Contato</title>
      </head>
      <body>
          <form action="{{ route('contato.salvar') }}" method="post">
              @csrf
              <label for="">Email: </label>
              <input type="text" name="email" id="email">
              <label for="">Telefone</label>
              <input type="text" name="telefone" id="telefone">
              <button type="submit">Salvar</button>
          </form>
      </body>
      </html>


