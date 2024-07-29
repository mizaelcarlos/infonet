Modificando Colunas
O changemétodo permite que você modifique o tipo e os atributos de colunas existentes. Por exemplo, você pode desejar aumentar o tamanho de uma stringcoluna. Para ver o changemétodo em ação, vamos aumentar o tamanho da namecoluna de 25 para 50. Para fazer isso, simplesmente definimos o novo estado da coluna e então chamamos o changemétodo:

<pre class="language-php">
  <code class="language-php">
     $table->string('name', 50)->change();
     $table->float('valor')->change();
  </code>
</pre>

