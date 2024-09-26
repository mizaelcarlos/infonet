### para criar herança de templates no laravel 

### Crie um diretorio dentro da pasta resources/views chamado de layouts e dentro dele crie o arquivo app.blade.php com o conteúdo abaixo:

```markdown

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title', 'Título Padrão')</title>
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css">
    @vite(['resources/js/app.js', 'resources/css/app.css'])
</head>
<body>
        @yield('content')

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.min.js"></script>
    @yield('scripts')
</body>
</html>

#### No arquivo que deseja herdar do layout basta colocar o trecho abaixo e remover as tags html, head e body, conforme exemplo abaixo:

```markdown

@extends('layouts.app')

<h2>Lista de Contatos</h2>

<table class="table">
    <thead>
        <tr>
        <th scope="col">ID</th>
        <th scope="col">EMAIL</th>
        <th scope="col">TELEFONE</th>
        <th scope="col">FOTO</th>
        <th scope="col">STATUS</th>
        <th scope="col">OPÇÕES</th>
        </tr>
    </thead>
    <tbody>
        @foreach($contatos as $contato)
            <tr>
                <th scope="row">{{ $contato->id }}</th>
                <td>{{ $contato->email }}</td>
                <td>{{ $contato->telefone }}</td>
                <td><img src="{{  asset('storage/' . $contato->foto) }}" alt="" width="100" height="100"></td>
                @if ($contato->status)
                <td>Ativo</td>
                @else
                <td>Inativo</td>
                @endif

                <td>
                    {{-- <div class="btns_formulario">
                        <a href="{{ route('contato.edit', $contato->id) }}">
                            <span>Editar</span>
                        </a>
                        <form action="{{ route('contato.destroy', $contato->id) }}" method="POST" style="display:inline;">
                            //@csrf
                            //@method('DELETE')
                            <button type="submit">Excluir</button>
                        </form>
                        <form action="{{ route('contato.atualizarStatus', $contato->id) }}" method="POST" style="display:inline;">
                            //@csrf
                            //@method('POST')
                            <button type="submit">Ativar</button>
                        </form>
                    </div> --}}
                </td>
            </tr>
            @endforeach
    </tbody>
</table>

{{-- <a href="{{ route('mensagem.index') }}">Contato</a> --}}

