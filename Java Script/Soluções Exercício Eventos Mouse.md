1 - Botão com alerta ao clicar
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Exemplo de Código</title>
<style>
  .code-block {
    background-color: #2d2d2d;
    color: #f8f8f2;
    padding: 10px;
    border-radius: 5px;
    font-family: monospace;
    position: relative;
  }
  .copy-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    cursor: pointer;
  }
</style>
</head>
<body>

<div class="code-block">
  <button class="copy-button" onclick="copyCode()">Copiar</button>
  <pre><code id="html-code">
	<button id="btnClick">Clique aqui</button>
	<script>
	  document.getElementById('btnClick').addEventListener('click', function() {
		alert('Botão clicado!');
	  });
	</script>
  </code></pre>
</div>

<script>
function copyCode() {
  var code = document.getElementById('html-code').innerText;
  navigator.clipboard.writeText(code).then(function() {
    alert('Código copiado para a área de transferência!');
  }, function(err) {
    console.error('Erro ao copiar o código: ', err);
  });
}
</script>

</body>
</html>
