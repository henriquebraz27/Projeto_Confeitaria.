
USE confeitaria;

CREATE TABLE Produtos(
codigo int(4) AUTO_INCREMENT,
produto varchar(30) NOT NULL,
preco varchar(20),
PRIMARY KEY (codigo)
);

CREATE TABLE usuarios(
codigo int(4) AUTO_INCREMENT,
email varchar(30) NOT NULL,
senha varchar(20),
PRIMARY KEY (codigo)
);



INSERT INTO Produtos(produto,preco) VALUES ( "Bolo de cenoura ","15,00") ;
INSERT INTO Produtos(produto,preco) VALUES ( "Rosquinha  ","4,00") ;
INSERT INTO Produtos(produto,preco) VALUES ( "Bolo de milho","15,00") ;
INSERT INTO Produtos(produto,preco) VALUES ( "Coca-Cola  ","9,00") ;
INSERT INTO Produtos(produto,preco) VALUES ( "Suco de Laranja","6,00") ;


UPDATE Produtos SET promo = "22/08/2021" where promo= "validade" ;

SELECT * FROM Produtos;

DROP TABLE produtos;