show databases;
create database fabiodb;
use fabiodb;

create table feedbacktb 
(
	nome varchar(60), 
    email varchar(60) NOT NULL,
    feedback varchar(300) NOT NULL
);

select * from feedbacktb;