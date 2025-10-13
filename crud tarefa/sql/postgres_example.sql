-- Exemplo DDL e DML para PostgreSQL

CREATE TABLE IF NOT EXISTS tarefas (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(200) NOT NULL,
  descricao TEXT,
  status VARCHAR(20) NOT NULL DEFAULT 'pendente',
  criado_em TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  atualizado_em TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

-- INSERT (retorna a linha inserida)
INSERT INTO tarefas (titulo, descricao, status)
VALUES ('Comprar material', 'Tinta e pincéis', 'pendente')
RETURNING id, titulo, descricao, status, criado_em;

-- SELECT
SELECT id, titulo, descricao, status, criado_em, atualizado_em FROM tarefas ORDER BY criado_em DESC;

-- UPDATE (retorna a linha atualizada)
UPDATE tarefas
SET titulo = 'Comprar material de pintura', status = 'em_progresso', atualizado_em = now()
WHERE id = 1
RETURNING id, titulo, descricao, status, atualizado_em;

-- DELETE (retorna a linha apagada)
DELETE FROM tarefas WHERE id = 1 RETURNING id, titulo, status;
