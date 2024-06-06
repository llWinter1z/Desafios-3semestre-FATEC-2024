show databases;
create database fabiodb;
use fabiodb;

create table feedbacktb 
(
	nome varchar(60), 
    email varchar(60),
    feedback varchar(300)
);

select * from feedbacktb;