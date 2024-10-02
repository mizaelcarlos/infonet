```sql

create database sistema;

use sistema;

create table usuario(
	id integer primary key auto_increment,
	nome varchar(200) not null,
	sobrenome varchar(200) null,
	email varchar(150) not null,
	senha varchar(250) not null,	
	);
	
alter table usuario(
	add column created_at timestamp null,
	add column update_a timestamp null
);

alter table usuario rename column update_a to update_at;


create table registro(
	id integer primary key auto_increment,
	nome varchar(120) not null,
	id_usuario integer,
	foreign key (id_usuario) references usuario (id)
	
	);

	
