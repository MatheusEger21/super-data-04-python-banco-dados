CREATE DATABASE loja_db;

-- apagar o banco de dados
-- DROP DATABASE loja_db

USE loja_db;
CREATE TABLE produtos(
    id INT PRIMARY KEY AUTO_INCREMENT, 
    descricao VARCHAR(200), 
    nome VARCHAR(50) NOT NULL
);
-- Apagar a tabela de produtos
-- DROP TABLE produtos;

SELECT id, nome, descricao FROM produtos;

INSERT INTO produtos (nome, descricao) VALUE ("Samsung Neo QLED 4k 65", "TV mais linda do mundo");

INSERT INTO produtos (nome, descricao) VALUES
("Positivo Dual Core 2Gb", "Computador melhor que tem"),
("Garmin Instict", NULL),
("Garmin Instict", "");

SELECT id, nome, descricao FROM produtos;

SELECT id, nome, descricao FROM produtos WHERE id = 4;

DELETE FROM produtos WHERE id = 4;

INSERT INTO produtos(nome, descricao) VALUE ("Sony Ericson w 200i", "Celular Infravermelho");

SELECT id, nome, descricao FROM produtos;

-- CONSULTAR OS PRODUTOS QUE TEM NULL NA DESCRICAO

SELECT id, nome, descricao 
    FROM produtos 
    WHERE descricao IS NULL;

UPDATE produtos 
    SET descricao = "GPS, LAranja" 
    WHERE id = 3;



-- CRUD (registros na tabela)
-- CREATE      INSERT
-- READ        SELECT
-- UPDATE      UPDATE
-- DELETE      DELETE


CREATE TABLE fornecedores(
    id int primary key AUTO_INCREMENT,
    cnpj varchar(18) not null,
    razao_social varchar(100) not null,
    nome_fantasia varchar(100) not null,
    cep varchar(10) not null,
    numero varchar(10)
);