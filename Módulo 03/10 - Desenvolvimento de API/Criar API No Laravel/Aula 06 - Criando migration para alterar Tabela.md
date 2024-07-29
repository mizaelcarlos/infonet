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

<div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>php</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copiar código</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-php"><span class="hljs-meta">&lt;?php</span>

<span class="hljs-keyword">use</span> <span class="hljs-title">Illuminate</span>\<span class="hljs-title">Database</span>\<span class="hljs-title">Migrations</span>\<span class="hljs-title">Migration</span>;
<span class="hljs-keyword">use</span> <span class="hljs-title">Illuminate</span>\<span class="hljs-title">Database</span>\<span class="hljs-title">Schema</span>\<span class="hljs-title">Blueprint</span>;
<span class="hljs-keyword">use</span> <span class="hljs-title">Illuminate</span>\<span class="hljs-title">Support</span>\<span class="hljs-title">Facades</span>\<span class="hljs-title">Schema</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AlterUsersTable</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Migration</span>
</span>{
    <span class="hljs-comment">/**
     * Aplicar as alterações à tabela.
     *
     * <span class="hljs-doctag">@return</span> void
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">up</span>(<span class="hljs-params"></span>)
    </span>{
        <span class="hljs-title class_">Schema</span>::<span class="hljs-title function_ invoke__">table</span>(<span class="hljs-string">'users'</span>, function (Blueprint <span class="hljs-variable">$table</span>) {
            <span class="hljs-comment">// Adiciona uma nova coluna</span>
            <span class="hljs-variable">$table</span>-&gt;<span class="hljs-keyword">string</span>(<span class="hljs-string">'tipo'</span>)-&gt;<span class="hljs-title function_ invoke__">nullable</span>();

            <span class="hljs-comment">// Remove uma coluna existente</span>
            <span class="hljs-variable">$table</span>-&gt;<span class="hljs-title function_ invoke__">dropColumn</span>(<span class="hljs-string">'old_column'</span>);
        });
    }

    <span class="hljs-comment">/**
     * Reverter as alterações.
     *
     * <span class="hljs-doctag">@return</span> void
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">down</span>(<span class="hljs-params"></span>)
    </span>{
        <span class="hljs-title class_">Schema</span>::<span class="hljs-title function_ invoke__">table</span>(<span class="hljs-string">'users'</span>, function (Blueprint <span class="hljs-variable">$table</span>) {
            <span class="hljs-comment">// Reverte a adição da coluna</span>
            <span class="hljs-variable">$table</span>-&gt;<span class="hljs-title function_ invoke__">dropColumn</span>(<span class="hljs-string">'age'</span>);

            <span class="hljs-comment">// Recria a coluna removida</span>
            <span class="hljs-variable">$table</span>-&gt;<span class="hljs-keyword">string</span>(<span class="hljs-string">'old_column'</span>)-&gt;<span class="hljs-title function_ invoke__">nullable</span>();
        });
    }
}
</code></div></div>
