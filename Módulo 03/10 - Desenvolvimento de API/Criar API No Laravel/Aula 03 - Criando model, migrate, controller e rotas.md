Criar primeiro model e migrate

<pre class="language-php">
  <code class="language-php">
    php artisan make:model Produto -m
  </code>
</pre>

Será criado uma classe chamada Produto.php no diretório app/Models

No model Produto.php , inserir o código abaixo:

protected $fillable = ['nome', 'valor' , 'descricao'];

Ele se refere aos campos prenchiveis, que serão utilizados no cadastro de um produto.


<pre class="language-php">
  <code class="language-php">
    namespace App\Models;
  
  use Illuminate\Database\Eloquent\Factories\HasFactory;
  use Illuminate\Database\Eloquent\Model;
  
  class Produto extends Model
  {
      use HasFactory;
  
      protected $fillable = ['nome', 'valor' , 'descricao'];
  }

  

  </code>
</pre>

Será criado também uma migrate relacionada ao model Produto no diretório database/migrations com um nome semelhante a:

2024_07_25_134630_create_produtos_table.php

Para inserir as colunas nome, valor e descrição , use as variáveis abaixo:

<pre class="language-php">
  <code class="language-php">
    public function up(): void
    {
        Schema::create('produtos', function (Blueprint $table) {
            $table->id();
            $table->string('nome');
            $table->integer('valor');
            $table->longText('descricao');
            $table->timestamps();
        });
    }
  </code>
</pre>

A documentação do laravel é muito extensa e podemos usar , então tudo que está relacionado a adicão novas colunas numa migration , pode ser acessar através da URL a seguir:

https://laravel.com/docs/11.x/migrations

para aplicar as alterações no banco de dados relacionado a migrate acima, rode o comando abaixo no terminal:

<pre class="language-php">
  <code class="language-php">
     php artisan migrate
  </code>
</pre>

Para criar um controller relacionado ao model Produto use o comando abaixo:

<pre class="language-php">
  <code class="language-php">
    php artisan make:controller ProdutoController --model=Produto
  </code>
</pre>


Abra o model Produto no diretório app/Models e insira o código seguinte abaixo de :

<pre class="language-php">
  <code class="language-php">
    <?php

namespace App\Models;

    use Illuminate\Database\Eloquent\Factories\HasFactory;
    use Illuminate\Database\Eloquent\Model;
    
    class Produto extends Model
    {
        use HasFactory;
    
        protected $fillable = ['nome', 'valor' , 'descricao'];
    }
  </code>
</pre>

Abra o controlador ProdutoController.php no diretório app/Http/Controllers 

Para configurar o método index , para consultar todos os produtos do banco de dados e retornar um Json , utilize o código abaixo:

<pre class="language-php">
  <code class="language-php">
   public function index()
    {
        $produtos = Produto::all();

        return response()->json([
            'status' => true,
            'produtos' => $produtos
        ]);
    }
    
  </code>
</pre>


Para criar uma rota e tornar a listagem feita anteriormente acessível , para que seja consultada por algum outro programa ou até mesmo pelo navegador , acesse o arquivo web.php que se encontra no diretório routes/

no inicio dele importe o controlador criado chamado de ProdutoController , colocando abaixo o seguinte código: 

<pre class="language-php">
  <code class="language-php">
   use Illuminate\Support\Facades\Route;
   use App\Http\Controllers\ProdutoController;
  </code>
</pre>



Agora vamos criar a nossa primeira rota GET, com o código abaixo:

<pre class="language-php">
  <code class="language-php">
   Route::get('/produtos', [ProdutoController::class, 'index']);
  </code>
</pre>



Agora vamos implementar o nosso método store, que irá permitir cadastrar novos produtos por meio do método POST.

Insira o código abaixo no método store do controlador ProdutoController

<pre class="language-php">
  <code class="language-php">
   public function store(Request $request)
    {
        $produto = Produto::create($request->all());

        return response()->json([
            'status' => true,
            'message' => "Produto Criado com sucesso!",
            'produto' => $produto
        ], 200);
    }
  </code>
</pre>


após isso insira a rota POST no arquivo web.php na 

<pre class="language-php">
  <code class="language-php">
    Route::post('/produtos', [ProdutoController::class, 'store']);
  </code>
</pre>


Para que possamos consumir as duas rotas criadas da API , precisamos gerar um token para passar no cabeçalho da requisição, esse token é gerado pela seguinte rota que tem que ser inserida no arquivo web.php

<pre class="language-php">
  <code class="language-php">
    Route::get('/token', function () {
      return csrf_token(); 
    });
  </code>
</pre>




Após isso gere a chave secreta da aplicação no arquivo .env usando o comando abaixo no terminal:

<pre class="language-php">
  <code class="language-php">
    php artisan key:generate
  </code>
</pre>
