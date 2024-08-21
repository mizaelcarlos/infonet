### 1 - Botão com alerta ao clicar

Você pode especificar a linguagem do código para destacar a sintaxe. Basta adicionar o nome da linguagem logo após os três acentos iniciais.

#### Código HTML com JavaScript:

```markdown
<button id="btnClick">Clique aqui</button>
<script>
  document.getElementById('btnClick').addEventListener('click', function() {
  alert('Botão clicado!');
  });
</script>
