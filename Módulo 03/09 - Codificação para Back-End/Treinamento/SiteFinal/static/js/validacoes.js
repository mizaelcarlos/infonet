$(document).ready(function() {
   
   $('#form_categoria').submit(function(event){
        let tipo = $('#tipo').val()
        let cnpj = $('#cnpj').val()
        if(tipo == ''){
            alert('Tipo obrigatório!')
            event.preventDefault();
        }
        if(cnpj.length != 14){
            alert('Campo CNPJ não possui 14 caracteres!')
            event.preventDefault();
        }
   });
});