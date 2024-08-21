function imprimirCabecalho() {
    // Seleciona o elemento com id 'cabecalho'
    const cabecalhoDiv = document.getElementById('cabecalho');

    // Cria um novo elemento de cabeçalho
    const h1 = document.createElement('h1');
    h1.textContent = 'Bem-vindo ao Meu Site!'; // Define o texto do cabeçalho

    // Adiciona o novo cabeçalho ao div
    cabecalhoDiv.appendChild(h1);
}

// Chama a função para imprimir o cabeçalho quando o script é carregado
imprimirCabecalho();