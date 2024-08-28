## Adicionar nova coluna status no módulo de Ordem de Serviços

### Adicionar nova migrate na tabela ordem_servicos

<pre class="language-php">
  <code class="language-php">
   php artisan make:migration alter_table_ordem_servicos_nova_coluna_status --table=ordem_servicos
  </code>
</pre>

### Abra o arquivo de migrate criado no diretório databases/migrations e insira o trecho abaixo:

<pre class="language-php">
  <code class="language-php">
     return new class extends Migration
    {
        /**
         * Run the migrations.
         */
        public function up(): void
        {
            Schema::table('ordem_servicos', function (Blueprint $table) {
                $table->boolean('status')->default(0);
        }
    
        /**
         * Reverse the migrations.
         */
        public function down(): void
        {
            Schema::table('ordem_servicos', function (Blueprint $table) {
                //
            });
        }
  </code>
</pre>

### após isso rode o comando abaixo para aplicar as alterações no banco de dados

<pre class="language-php">
  <code class="language-php">
      php artisan migrate
  </code>
</pre>

### Na classe OrdemServico.php no diretório app/Models adicionar a nova coluna nos campos prenchíveis

 
<pre class="language-php">
  <code class="language-php">
    protected $fillable = ['cliente_id','empresa_id','servico_id','data','data_finalizacao', 'status'];
  </code>
</pre>


