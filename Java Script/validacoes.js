$(document).ready(function() {
   //jquery
   let nome2 = document.getElementById("#nome").value //javaScript

   $('#form').submit(function(event){
        
   });

   $('$btnSalvar').click(function(event){
    let nome = $('#nome').val();
    if(nome == ''){
        alert('Nome é obrigatório!')
        event.preventDefault();
    }
   });


   
});