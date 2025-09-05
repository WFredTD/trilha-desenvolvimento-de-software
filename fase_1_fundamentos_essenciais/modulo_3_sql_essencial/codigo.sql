-- Database: gerenciador_livros

-- DROP DATABASE IF EXISTS gerenciador_livros;

CREATE DATABASE gerenciador_livros
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE IF NOT EXISTS autores(
	id SERIAL PRIMARY KEY,
	nome TEXT NOT NULL,
	nacionalidade TEXT NOT NULL,
	data_nascimento DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS livros(
	id SERIAL PRIMARY KEY,
	titulo TEXT NOT NULL,
	ano_publicacao INT NOT NULL,
	id_autor INT NOT NULL, -- É do tipo INT para ser consistente com a chave primária
	preco DECIMAL NOT NULL,
	FOREIGN KEY (id_autor) REFERENCES autores(id)
);

INSERT INTO autores (
	nome,
	nacionalidade,
	data_nascimento
)
VALUES
	(
		'J.R.R. Tolkien',
		'Britânica',
		'1892-01-03'
	),
	(
		'Isaac Asimov',
		'Americana',
		'1920-01-02'
	),
	(
		'Stephen King',
		'Americana',
		'1947-09-21'
	);


INSERT INTO livros (
	titulo,
	ano_publicacao,
	id_autor,
	preco
)
VALUES
	(
		'O Senhor dos Anéis',
		1954,
		1,
		89.90
	),
	(
		'Eu, Robô',
		1950,
		2,
		45.50
	),
	(
		'O Hobbit',
		1937,
		1,
		55.00
	),
	(
		'A Fundação',
		1951,
		2,
		59.90
	),
	(
		'A Torre Negra: O Pistoleiro',
		1982,
		3,
		75.00
	);

SELECT * FROM autores;

SELECT * FROM livros;

SELECT *
FROM livros
WHERE titulo = 'O Senhor dos Anéis';

UPDATE livros
SET preco = 79.90 
WHERE id = 1;

DELETE FROM livros WHERE id =5;

DELETE FROM autores WHERE id = 3;


SELECT
	livros.titulo,
	autores.nome
FROM
	livros
JOIN
	autores
ON
	livros.id_autor = autores.id;


SELECT
	COUNT(*) AS numero_de_livros
FROM
	livros;


SELECT
	AVG(preco)
FROM
	livros;


SELECT
	MIN(ano_publicacao)
FROM
	livros;


SELECT
	a.nome AS nome,
	COUNT(*) AS numero_de_livros
FROM
	autores AS a
JOIN
	livros AS l
ON
	a.id = l.id_autor
GROUP BY
	nome
ORDER BY
	nome;


SELECT *
FROM livros
WHERE ano_publicacao > 1950
ORDER BY ano_publicacao DESC;