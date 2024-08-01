Modificando Colunas

Para fazer modificação em colunas , crie uma nova migrate e aidicone as configuração nova das colunas no método up() da migrate:

<pre class="language-php">
  <code class="language-php">
    php artisan make:migration rename_column_in_table_name
  </code>
</pre>

O changemétodo permite que você modifique o tipo e os atributos de colunas existentes. Por exemplo, você pode desejar aumentar o tamanho de uma coluna string . Para ver o changemétodo em ação, vamos aumentar o tamanho da namecoluna de 25 para 50. Para fazer isso, simplesmente definimos o novo estado da coluna e então chamamos o changemétodo:

Edite a nova migration:


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

<pre class="language-php">
  <code class="language-php">
      $table->renameColumn('old_column_name', 'new_column_name');
  </code>
</pre>


Abra o arquivo da nova migration que foi criada. Ele estará localizado na pasta database/migrations e terá um nome semelhante a xxxx_xx_xx_xxxxxx_rename_column_in_table_name.php.

Edite o arquivo para adicionar o código necessário para renomear a coluna. Aqui está um exemplo:

<pre class="language-php">
  <code class="language-php">
      $table->renameColumn('old_column_name', 'new_column_name');
  </code>
</pre>


Substitua 'table_name' pelo nome da tabela em que você deseja renomear a coluna.
Substitua 'old_column_name' pelo nome atual da coluna que você deseja renomear.
Substitua 'new_column_name' pelo novo nome da coluna.

Execute a migration:

Após definir a migration, você precisa executá-la para aplicar as alterações ao banco de dados. No terminal, execute:

<pre class="language-php">
  <code class="language-php">
    php artisan migrate
  </code>
</pre>

