$(document).ready(function() {
   
    $('#form_empresa').submit(function(event){
         let cnpj = $('#cnpj').val()
         if(cnpj.length != 14){
             alert('Campo CNPJ não possui 14 caracteres!')
             event.preventDefault();
         }
    });
 });