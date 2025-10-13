# CRUD de exemplo (SQLite)

Este repositório contém um exemplo simples em Python que cria uma tabela fictícia `tarefas` e executa as quatro operações básicas do CRUD (Create, Read, Update, Delete) usando SQLite embutido — sem dependências externas.

Arquivos:
- `src/crud_sqlite.py` - script Python que cria a tabela e executa INSERT / SELECT / UPDATE / DELETE, exibindo os resultados.
- `sql/postgres_example.sql` - exemplo DDL/DML para PostgreSQL.
- `sql/mysql_example.sql` - exemplo DDL/DML para MySQL.

Pré-requisitos
- Python 3.6+ instalado no sistema.

Como rodar (PowerShell)

```powershell
# Navegue até a pasta do projeto
cd "c:\Users\Pichau\OneDrive\Desktop\crud tarefa"

# Rode o script
python .\src\crud_sqlite.py
```

O script criará um arquivo `tarefas.db` na pasta `src` e imprimirá no terminal cada etapa do CRUD.

Se preferir usar PostgreSQL ou MySQL, veja os exemplos em `sql/`.
