Passo 1: Criar a Migration
Você pode criar uma nova migration usando o comando Artisan. No terminal, execute o seguinte comando, substituindo alter_table_name pelo nome descritivo da sua migration:

<pre class="language-php">
  <code class="language-php">
   php artisan make:migration alter_table_name --table=table_name
  </code>
</pre>

Por exemplo, se você deseja alterar uma tabela chamada categoria, você pode nomear a migration alter_categoria_table:

<pre class="language-php">
  <code class="language-php">
   php artisan make:migration alter_table_categoria --table=categoria
  </code>
</pre>

Passo 2: Editar a Migration
Após criar a migration, vá até o arquivo da migration que foi gerado. O arquivo estará localizado na pasta database/migrations e terá um nome parecido com YYYY_MM_DD_HHMMSS_alter_users_table.php.

Abra o arquivo da migration e defina as alterações desejadas na tabela. O método up é usado para aplicar as alterações, enquanto o método down é usado para reverter as alterações, se necessário.

Aqui está um exemplo de como adicionar uma coluna age e remover uma coluna old_column:

<pre class="language-php">
  <code class="language-php">

  use Illuminate\Database\Migrations\Migration;
  use Illuminate\Database\Schema\Blueprint;
  use Illuminate\Support\Facades\Schema;

    return new class extends Migration
    {
        /**
         * Run the migrations.
         */
        public function up(): void
        {
            Schema::table('categoria', function (Blueprint $table) {
                $table->string('tipo');
                $table->dropColumn('nome');
            });
        }
    
        /**
         * Reverse the migrations.
         */
        public function down(): void
        {
            Schema::table('categoria', function (Blueprint $table) {
                $table->string('nome');
                $table->dropColumn('tipo');
            });
        }
    };

  </code>
</pre>

Passo 3: Rodar a Migration
Depois de definir as alterações na migration, aplique as mudanças ao banco de dados usando o comando Artisan:

<pre class="language-php">
  <code class="language-php">
   php artisan migrate
  </code>
</pre>

Passo 4: Reverter a Migration (se necessário)
Se precisar reverter as alterações feitas por uma migration, use o comando:

<pre class="language-php">
  <code class="language-php">
  php artisan migrate:rollback
  </code>
</pre>
