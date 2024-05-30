# [-] | Alterando e Excluindo colunas

```bash
# -- Criando nova tabela --

CREATE TABLE usuarios_nova (
  id INT,
  nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
  email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de e-mail do usuário',
  data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário',
  endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do Cliente'
);

# -- Migrando os dados --

INSERT INTO usuarios_nova
SELECT * from usuarios;

# -- Excluindo tabela anterior --
DROP table usuarios;

# -- Renomeando nova tabela --
ALTER TABLE usuarios_nova RENAME usuarios;


# -- Ou opção 2 : Alterar tamanho da coluna endereço -- 
ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(100);
```

# [-] | Chaves Primarias e Estrangeiras

```bash
# Primary Key--
# Tabela "usuarios"
ALTER TABLE usuarios
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

# Tabela "destinos"
ALTER TABLE destinos
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

# Tabela "reservas"
ALTER TABLE reservas
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

# -- Exemplos --

# -- Inserção na tabela "usuarios"
INSERT INTO usuarios (nome, email, data_nascimento, endereco)
VALUES ('João Maria', 'joaomaria@example.com', '1990-01-01', 'Rua A, 123');

# -- Inserção na tabela "destinos"
INSERT INTO destinos (nome, descricao)
VALUES ('Praia Teste', 'Destino paradisíaco com belas praias.');

# -- Inserção na tabela "reservas"
INSERT INTO reservas (id_usuario, id_destino, data, status)
VALUES (4, 4, '2023-07-01', 'pendente');

# -- Chaves estrangeiras --

# -- Adicionando chave estrangeira na tabela "reservas" referenciando a tabela "usuarios"
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id);

# -- Adicionando chave estrangeira na tabela "reservas" referenciando a tabela "destinos"
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destino) REFERENCES destinos(id);

# -- Alterando a restrição da chave estrangeira "fk_reservas_usuarios" na tabela "reservas" para ON DELETE CASCADE
ALTER TABLE reservas
DROP FOREIGN KEY fk_reservas_usuarios;

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
ON DELETE CASCADE;
```

# [-] | Normalização de Dados

## Adicionando colunas na tabela 'usuarios'

```bash
ALTER TABLE usuarios
ADD rua VARCHAR(50) 
ADD numero VARCHAR(10) 
ADD cidade VARCHAR(50) 
ADD estado VARCHAR(20)
```

## Copia os dados da tabela original para a nova tabela

```bash
UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1),
    numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1),
    cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1),
    estado = SUBSTRING_INDEX(endereco, ',', -1);
```

## Exclusão da coluna "endereco" da tabela original

```bash
ALTER TABLE usuarios
DROP COLUMN endereco;
```

## Consultas com junções e Subconsultas

```bash
INSERT INTO usuarios (nome, email, data_nascimento, rua, numero, cidade, estado) VALUES ('Usuario sem reservas', 'semreservar@teste.com', '1990-10-10', 'Rua','123','cidade','estado');

# -- Traz apenas os usuario com reservas
SELECT * FROM usuarios us
INNER JOIN reservas rs
	ON us.id = rs.id_usuario;

# -- Traz todos os usuario e suas reservas se tiver
SELECT * FROM usuarios us
INNER JOIN reservas rs
	ON us.id = rs.id_usuario;

INSERT INTO viagens.destinos ( nome, descricao) VALUES 
('Deestino sem reserva', 'Uma bela praia com areias brancas e mar cristalino')

# -- Tras todos os destinos e as reservas se tiverem -- 
SELECT * FROM reservas rs
RIGHT JOIN destinos des
	ON des.id = rs.id_destino;

# -- Produz o mesmo resultado que a anterior
SELECT * FROM destinos des
LEFT JOIN reservas rs
	ON des.id = rs.id_destino;

# -- SUb consultas --

# -- Usuários que não fizeram nenhuma reserva
SELECT nome
FROM usuarios
WHERE id NOT IN (SELECT id_usuario FROM reservas);

# -- Subconsulta para encontrar os destinos menos populares (com menos reservas)
SELECT nome
FROM destinos
WHERE id NOT IN (SELECT id_destino FROM reservas)
ORDER BY id;

# -- contagem de reservas por usuario
SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reservas
FROM usuarios;
```

## Funções agregadas e agrupamento de resultados

```bash
SELECT COUNT(*) FROM usuarios;

# -- Media da idade dos usuarios
SELECT AVG(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS idade
FROM usuarios;

# -- Soma da idade dos usuarios
SELECT SUM(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

# -- Menor Idade
SELECT MIN(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

# -- Maior Idade
SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

# -- Calcula quantidade de reservas por destino --
SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino ;


# -- Limit
SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino LIMIT 1 OFFSET 2;

SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino LIMIT 1;

# -- Ordenação
SELECT nome
FROM usuarios
ORDER BY nome;

SELECT nome, data_nascimento
FROM usuarios
ORDER BY data_nascimento, nome;

SELECT nome, data_nascimento
FROM usuarios
ORDER BY data_nascimento, nome DESC;
```

## Índices

```bash
-- Inserindo massa de dados --

INSERT INTO usuarios (nome, email, data_nascimento, rua) VALUES
('João Silva', 'joao.silva@example.com', '1990-01-01', 'Rua A'),
('Maria Santos', 'maria.santos@example.com', '1992-03-15', 'Rua B'),
('Pedro Almeida', 'pedro.almeida@example.com', '1985-07-10', 'Rua C'),
('Ana Oliveira', 'ana.oliveira@example.com', '1998-12-25', 'Rua D'),
('Carlos Pereira', 'carlos.pereira@example.com', '1991-06-05', 'Rua E'),
('Laura Mendes', 'laura.mendes@example.com', '1994-09-12', 'Rua F'),
('Fernando Santos', 'fernando.santos@example.com', '1988-02-20', 'Rua G'),
('Mariana Costa', 'mariana.costa@example.com', '1997-11-30', 'Rua H'),
('Ricardo Rodrigues', 'ricardo.rodrigues@example.com', '1993-04-18', 'Rua I'),
('Camila Alves', 'camila.alves@example.com', '1989-08-08', 'Rua J'),
('Bruno Carvalho', 'bruno.carvalho@example.com', '1995-03-25', 'Rua K'),
('Amanda Silva', 'amanda.silva@example.com', '1996-12-02', 'Rua L'),
('Paulo Mendonça', 'paulo.mendonca@example.com', '1999-07-20', 'Rua M'),
('Larissa Oliveira', 'larissa.oliveira@example.com', '1987-10-15', 'Rua N'),
('Fernanda Sousa', 'fernanda.sousa@example.com', '1992-05-08', 'Rua O'),
('Gustavo Santos', 'gustavo.santos@example.com', '1993-09-18', 'Rua P'),
('Helena Costa', 'helena.costa@example.com', '1998-02-22', 'Rua Q'),
('Diego Almeida', 'diego.almeida@example.com', '1991-11-27', 'Rua R'),
('Juliana Lima', 'juliana.lima@example.com', '1997-04-05', 'Rua S'),
('Rafaela Silva', 'rafaela.silva@example.com', '1996-01-10', 'Rua T'),
('Lucas Pereira', 'lucas.pereira@example.com', '1986-08-30', 'Rua U'),
('Fábio Rodrigues', 'fabio.rodrigues@example.com', '1989-03-12', 'Rua V'),
('Isabela Santos', 'isabela.santos@example.com', '1994-12-07', 'Rua W'),
('André Alves', 'andre.alves@example.com', '1995-09-28', 'Rua X'),
('Clara Carvalho', 'clara.carvalho@example.com', '1990-02-15', 'Rua Y'),
('Roberto Mendes', 'roberto.mendes@example.com', '1992-07-21', 'Rua Z'),
('Mariana Oliveira', 'mariana.oliveira@example.com', '1997-05-03', 'Av. A'),
('Gustavo Costa', 'gustavo.costa@example.com', '1998-11-16', 'Av. B'),
('Lara Sousa', 'lara.sousa@example.com', '1993-06-09', 'Av. C'),
('Pedro Lima', 'pedro.lima@example.com', '1996-09-27', 'Av. D');




EXPLAIN SELECT * FROM usuarios WHERE nome = "Maria";

EXPLAIN SELECT * FROM usuarios us
INNER JOIN reservas rs
ON us.id = rs.id_usuario
WHERE nome = "Maria";


CREATE INDEX idx_nome ON usuarios (nome);

EXPLAIN SELECT * FROM usuarios WHERE nome = "Maria";
```