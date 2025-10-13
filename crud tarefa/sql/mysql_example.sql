-- Exemplo DDL e DML para MySQL

CREATE TABLE IF NOT EXISTS tarefas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(200) NOT NULL,
  descricao TEXT,
  status VARCHAR(20) NOT NULL DEFAULT 'pendente',
  criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- INSERT
INSERT INTO tarefas (titulo, descricao, status)
VALUES ('Comprar material', 'Tinta e pincéis', 'pendente');

-- obter id inserido na mesma sessão (driver):
-- SELECT LAST_INSERT_ID();

-- SELECT
SELECT id, titulo, descricao, status, criado_em, atualizado_em FROM tarefas ORDER BY criado_em DESC;

-- UPDATE
UPDATE tarefas
SET titulo = 'Comprar material de pintura', status = 'em_progresso'
WHERE id = 1;

-- DELETE
DELETE FROM tarefas WHERE id = 1;
