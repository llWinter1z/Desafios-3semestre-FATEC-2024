show databases; --mostra os bancos de dados--
create database fabiodb; --cria o banco de dados--
use fabiodb; --usa o banco de dados--

--cria uma tabela--
create table feedbacktb 
(
	nome varchar(60), 
    email varchar(60),
    feedback varchar(300)
);

select * from feedbacktb;