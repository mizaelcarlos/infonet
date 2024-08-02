Vamos criar um model chamado Serviço, para criar utilize o código abaixo:

<pre class="language-php">
  <code class="language-php">
      php artisan make:model Servico -m
  </code>
</pre>

O código acima irá criar o arquivo Servico.php e a migrate relacionada a esse model.

Abra o arquivo de migrate criado no diretório databases/migrations e insira o trecho abaixo:

<pre class="language-php">
  <code class="language-php">
      public function up(): void
    {
        Schema::create('servicos', function (Blueprint $table) {
            $table->id();
            $table->string('tipo');
            $table->float('valor');
            $table->unsignedBigInteger('empresa_id')->nullable();
            $table->unsignedBigInteger('categoria_id')->nullable();
            $table->foreign('empresa_id')
                ->references('id')
                ->on('empresas')
                ->onDelete('cascade');
            $table->foreign('categoria_id')
                ->references('id')
                ->on('categorias')
                ->onDelete('cascade');
            $table->timestamps();
        });
    }
  </code>
</pre>

O que fizemos foi inserir 4 atributos que são eles, tipo, valor, empresa_id e categoria_id e depois fizemos o relacionamento dos atributos
empresa_id e categoria_id com a sua tabela relacionada, assim eles (empresa_id e categoria_id)se tornaram chave estrangeira que fazem relacionamento com
as tabelas (empresas,categorias) respectivamente.

Após isso , basta rodar o comando abaixo pra aplicar as migrations no banco de dados:

 
<pre class="language-php">
  <code class="language-php">
      php artisan migrate
  </code>
</pre>

Após isso , vamos fazer o relacionamento nos models, declarando que as classes vão entender o relacionamento que existe no banco de dados.

Para isso , basta abrir o model Servico.php e inserir o código abaixo:

<pre class="language-php">
  <code class="language-php">
      class Servico extends Model
      {
          use HasFactory;
      
          protected $fillable = ['tipo', 'valor', 'empresa_id', 'categoria_id'];
      
          public function empresa()
          {
              return $this->belongsTo(Empresa::class);
          }
      
          public function categoria()
          {
              return $this->belongsTo(Categoria::class);
          }
      }
  </code>
</pre>

os métodos empresa() e categoria() significam que :

public function empresa(): Define um método chamado empresa que estabelece um relacionamento entre o modelo Servico e o modelo Empresa.
return $this->belongsTo(Empresa::class);: Indica que o modelo Servico pertence a uma Empresa. O método belongsTo define um relacionamento de muitos-para-um, onde várias instâncias do modelo Servico estão associadas a uma única instância do modelo Empresa. Isso permite acessar a empresa associada a um serviço específico.

public function categoria(): Define um método chamado categoria que estabelece um relacionamento entre o modelo Servico e o modelo Categoria.
return $this->belongsTo(Categoria::class);: Indica que o modelo Servico pertence a uma Categoria. Semelhante ao relacionamento com a Empresa, o método belongsTo define um relacionamento de muitos-para-um, onde várias instâncias do modelo Servico estão associadas a uma única instância do modelo Categoria. Isso permite acessar a categoria associada a um serviço específico.

No model Categoria.php , insira o código abaixo:

<pre class="language-php">
  <code class="language-php">
      class Categoria extends Model
      {
          use HasFactory;
      
          protected $fillable = ['tipo'];
      
          public function servicos()
          {
              return $this->hasMany(Servico::class);
          }
      }
  </code>
</pre>

public function servicos(): Define um método chamado servicos que estabelece um relacionamento entre o modelo Categoria e o modelo Servico.
return $this->hasMany(Servico::class);: Indica que uma instância do modelo Categoria pode ter muitos Servicos. O método hasMany define um relacionamento de um-para-muitos, onde uma instância do modelo Categoria está associada a várias instâncias do modelo Servico. Isso permite acessar todos os serviços associados a uma categoria específica.

No model Empresa.php , insira o código abaixo:

<pre class="language-php">
  <code class="language-php">
      class Empresa extends Model
      {
          use HasFactory;
      
          protected $fillable = ['razao_social', 'cnpj'];
      
          public function servicos()
          {
              return $this->hasMany(Servico::class);
          }
      }
  </code>
</pre>

public function servicos(): Define um método chamado servicos que estabelece um relacionamento entre o modelo Empresa e o modelo Servico.
return $this->hasMany(Servico::class);: Indica que uma Empresa pode ter muitos Servicos. O método hasMany define um relacionamento de um-para-muitos, onde uma instância do modelo Empresa está associada a várias instâncias do modelo Servico.

Após isso vamos criar o ServicoController usando o comando abaixo:

<pre class="language-php">
  <code class="language-php">
       php artisan make:controller ServicoController --model=Servico
  </code>
</pre>

Após isso abra o arquivo e insira o código abaixo:

<pre class="language-php">
  <code class="language-php">
       public function index()
    {
        $servicos = Servico::with('empresa','categoria')->get();
        return response()->json([
            'status' => True,
            'servicos' => $servicos
        ]);
    }
  </code>
</pre>

<pre class="language-php">
  <code class="language-php">
      public function store(Request $request)
      {
          $servico = Servico::create($request->all());
  
          return response()->json([
              'status' => true,
              'message' => "Servico criada com sucesso!",
              'servico' => $servico
          ], 200);
      }
  </code>
</pre>

Após isso abra o arquivo de rotas web.php e insira as rotas referente ao métodos index e store:



Route::get('/servicos', [ServicoController::class, 'index']);
Route::post('/servicos', [ServicoController::class, 'store']);

após isso , basta testar o cadastro e a listagem de serviços usando o Postman.
