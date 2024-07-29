Modificando Colunas

Para fazer modificação em colunas , crie uma nova migrate e aidicone as configuração nova das colunas no método up() da migrate:

O changemétodo permite que você modifique o tipo e os atributos de colunas existentes. Por exemplo, você pode desejar aumentar o tamanho de uma coluna string . Para ver o changemétodo em ação, vamos aumentar o tamanho da namecoluna de 25 para 50. Para fazer isso, simplesmente definimos o novo estado da coluna e então chamamos o changemétodo:

<pre class="language-php">
  <code class="language-php">
    $table->string('name', 50)->change();
  </code>
</pre>

Ou voc~e pode querer mudar o tipo da coluna, basta chamar o novo tipo , informar o nome da coluna e chamar o método change.
<pre class="language-php">
  <code class="language-php">
     $table->float('valor')->change();
  </code>
</pre>


