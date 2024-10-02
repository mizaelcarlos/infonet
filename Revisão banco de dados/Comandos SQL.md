### Comando para remover o banco de dados.

drop database nome_do_banco;

### comando para remover tabela do banco de dados

drop table nome_tabela;

### Comando para remover coluna de tabela

alter table nome_tabela drop column nome_coluna;

### Comando para inserir registros na tabela

insert into nome_tabela (coluna1,coluna2,coluna3) values (value1,value2,value3);

Ex:

INSERT INTO usuario (nome, sobrenome,email,senha,created_at,update_at) VALUES ('Mizael','Carlos','mizaelcarlos44@gmail.com','teste123','2024-10-02 07:57:00','2024-10-02 07:57:00');
