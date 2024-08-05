Para criar autenticação em uma API usando o Laravel 11, você pode utilizar o pacote Laravel Sanctum, que é uma solução simples para autenticação de API, ideal para aplicações SPA (Single Page Applications) e APIs simples. Aqui está um passo a passo para configurar a autenticação com o Laravel Sanctum:

Passo 1: Instalação do Laravel Sanctum
Primeiro, você precisa instalar o Laravel Sanctum no seu projeto Laravel. Execute o seguinte comando para adicionar o pacote via Composer:

<pre class="language-php">
  <code class="language-php">
      composer require laravel/sanctum
  </code>
</pre>

Passo 2: Publicar a Configuração
Depois de instalar o Sanctum, publique o arquivo de configuração usando o comando:


<pre class="language-php">
  <code class="language-php">
     php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
  </code>
</pre>

Isso criará o arquivo de configuração config/sanctum.php.

Passo 3: Migrar o Banco de Dados
Sanctum precisa de uma tabela para armazenar tokens. Execute as migrações para criar essa tabela:

<pre class="language-php">
  <code class="language-php">
     php artisan migrate
  </code>
</pre>

Passo 4: Configurar o Middleware
Para proteger as rotas da API com Sanctum, adicione o middleware sanctum ao grupo de middleware api no arquivo app/Http/Kernel.php. Adicione a seguinte linha ao array $middlewareGroups['api']:

<pre class="language-php">
  <code class="language-php">
     'api' => [
    \Laravel\Sanctum\Http\Middleware\EnsureFrontendRequestsAreStateful::class,
    'throttle:api',
    \Illuminate\Routing\Middleware\SubstituteBindings::class,
],
  </code>
</pre>

Passo 5: Configurar o Model User
O modelo User deve usar o trait HasApiTokens. Abra o arquivo app/Models/User.php e adicione o trait:

<pre class="language-php">
  <code class="language-php">
    namespace App\Models;

    use Illuminate\Foundation\Auth\User as Authenticatable;
    use Laravel\Sanctum\HasApiTokens;
    
    class User extends Authenticatable
    {
        use HasApiTokens, Notifiable;
  </code>
</pre>

Passo 6: Criar Rotas de Autenticação
Você pode criar rotas para registro e login no arquivo routes/api.php. Aqui está um exemplo básico:

<pre class="language-php">
  <code class="language-php">
   use Illuminate\Support\Facades\Route;
    use App\Http\Controllers\AuthController;
    
    Route::post('register', [AuthController::class, 'register']);
    Route::post('login', [AuthController::class, 'login']);
    Route::middleware('auth:sanctum')->get('user', function (Request $request) {
        return $request->user();
    });
  </code>
</pre>

Passo 7: Criar o Controlador de Autenticação
Crie um controlador para gerenciar o registro e login. Você pode gerar um controlador usando Artisan:

<pre class="language-php">
  <code class="language-php">
  php artisan make:controller AuthController
  </code>
</pre>

Depois, implemente os métodos register e login no controlador. Aqui está um exemplo básico:


<pre class="language-php">
  <code class="language-php">
    namespace App\Http\Controllers;

    use Illuminate\Http\Request;
    use App\Models\User;
    use Illuminate\Support\Facades\Hash;
    use Illuminate\Support\Facades\Validator;
    use Illuminate\Support\Str;
    
    class AuthController extends Controller
    {
        public function register(Request $request)
        {
            $validator = Validator::make($request->all(), [
                'name' => 'required|string|max:255',
                'email' => 'required|string|email|max:255|unique:users',
                'password' => 'required|string|min:8|confirmed',
            ]);
    
            if ($validator->fails()) {
                return response()->json($validator->errors(), 422);
            }
    
            $user = User::create([
                'name' => $request->name,
                'email' => $request->email,
                'password' => Hash::make($request->password),
            ]);
    
            return response()->json([
                'user' => $user,
                'token' => $user->createToken('API Token')->plainTextToken,
            ], 201);
        }
    
        public function login(Request $request)
        {
            $validator = Validator::make($request->all(), [
                'email' => 'required|string|email',
                'password' => 'required|string',
            ]);
    
            if ($validator->fails()) {
                return response()->json($validator->errors(), 422);
            }
    
            $user = User::where('email', $request->email)->first();
    
            if (!$user || !Hash::check($request->password, $user->password)) {
                return response()->json(['message' => 'Invalid credentials'], 401);
            }
    
            return response()->json([
                'user' => $user,
                'token' => $user->createToken('API Token')->plainTextToken,
            ]);
        }
    }
  </code>
</pre>

Passo 8: Testar a API
Agora você pode testar a API usando ferramentas como Postman ou CURL. Faça requisições para os endpoints de registro e login para criar tokens e autenticar usuários.
