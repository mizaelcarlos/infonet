Professor - Mizael Carlos

O Laravel Eloquent é uma maneira fácil de interagir com seu banco de dados. É um mapeador objeto-relacional (ORM) que simplifica as complexidades dos bancos de dados, fornecendo um modelo para interagir com as tabelas.

Como tal, o Laravel Eloquent tem excelentes ferramentas para criar e testar APIs para dar suporte ao seu desenvolvimento. Neste artigo prático, você verá como é fácil criar e testar APIs usando o Laravel.

Nesta demonstração, você começará criando um modelo que pode ser usado para criar a API e a tabela do banco de dados. Daí verá como adicionar um controlador como camada de lógica de negócios e uma rota para concluir a API. Em seguida, você aprenderá a realizar testes de APIs usando o Postman antes de finalmente se concentrar na autenticação e no tratamento de erros.

Pré-requisitos , Para começar, eis o que você precisará:

Laravel ultima versão
Composer
Postman
XAMPP ou Wampserver
Conhecimento básico de APIs e PHP


Comece criando um novo projeto Laravel usando composer:

composer create-project laravel/laravel laravel-api

Para iniciar o servidor, execute o seguinte comando, que roda o servidor de aplicativos na porta 8000:

cd laravel-api

php artisan serve

Você deverá ver a tela a seguir:

