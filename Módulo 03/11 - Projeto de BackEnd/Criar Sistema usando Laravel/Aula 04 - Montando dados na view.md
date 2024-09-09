O retorno do método index no controller será conforme abaixo:

Exemplo:

<pre class="language-php">
  <code class="language-php">
    public function index()
    {
        $contatos = Contato::all();

        return view('contato.index', ['contatos' => $contatos]);
    }
  </code>
</pre>

Para o exemplo acima arquivo de template deverá está na pasta resources/views/contato/index.blade.php, segue HTML:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h2>Lista de Contatos</h2>

    <table class="table">
        <thead>
            <tr>
            <th scope="col">ID</th>
            <th scope="col">TELEFONE</th>
            <th scope="col">EMAIL</th>
            </tr>
        </thead>
        <tbody>
            @foreach($contatos as $contato)
                <tr>
                    <th scope="row">{{ $contato->id }}</th>
                    <td>{{ $contato->telefone }}</td>
                    <td>{{ $contato->email }}</td>
                    <td>
                        <div class="btns_formulario">
                            <a href="">
                                <span>Editar Cliente</span>
                            </a>
                            <a href="">
                                <span>Excluir Cliente</span>
                            </a>
                        </div>
                    </td>
                </tr>
                @endforeach
        </tbody>
    </table>
</body>
</html>
