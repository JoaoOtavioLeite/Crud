#!/usr/bin/env python3
"""
Exemplo mínimo de CRUD usando sqlite3 (Python padrão).
Cria a tabela `tarefas` e mostra operações: inserir, ler, atualizar e apagar.
"""
from pathlib import Path
import sqlite3
import pprint

DB_PATH = Path(__file__).parent / "tarefas.db"
pp = pprint.PrettyPrinter(indent=2)


def get_conn():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def create_table(conn: sqlite3.Connection):
    sql = """
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        status TEXT NOT NULL DEFAULT 'pendente',
        criado_em TEXT NOT NULL DEFAULT (datetime('now')),
        atualizado_em TEXT NOT NULL DEFAULT (datetime('now'))
    );
    """
    conn.execute(sql)
    conn.commit()


def create_tarefa(conn: sqlite3.Connection, titulo: str, descricao: str = None, status: str = 'pendente') -> int:
    cur = conn.execute(
        "INSERT INTO tarefas (titulo, descricao, status) VALUES (?, ?, ?)",
        (titulo, descricao, status),
    )
    conn.commit()
    return cur.lastrowid


def get_all(conn: sqlite3.Connection):
    cur = conn.execute("SELECT * FROM tarefas ORDER BY criado_em DESC")
    return [dict(row) for row in cur.fetchall()]


def get_by_id(conn: sqlite3.Connection, tarefa_id: int):
    cur = conn.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
    row = cur.fetchone()
    return dict(row) if row else None


def update_tarefa(conn: sqlite3.Connection, tarefa_id: int, **fields) -> dict:
    # fields: titulo, descricao, status
    if not fields:
        raise ValueError("Nenhum campo para atualizar")
    allowed = {"titulo", "descricao", "status"}
    set_parts = []
    params = []
    for k, v in fields.items():
        if k not in allowed:
            continue
        set_parts.append(f"{k} = ?")
        params.append(v)
    if not set_parts:
        raise ValueError("Nenhum campo válido para atualizar")
    # atualiza timestamp
    set_parts.append("atualizado_em = datetime('now')")
    sql = f"UPDATE tarefas SET {', '.join(set_parts)} WHERE id = ?"
    params.append(tarefa_id)
    cur = conn.execute(sql, tuple(params))
    conn.commit()
    if cur.rowcount == 0:
        return None
    return get_by_id(conn, tarefa_id)


def delete_tarefa(conn: sqlite3.Connection, tarefa_id: int) -> dict:
    # retornar a linha apagada
    row = get_by_id(conn, tarefa_id)
    if not row:
        return None
    conn.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    conn.commit()
    return row


def main():
    print("Banco:", DB_PATH)
    conn = get_conn()
    try:
        create_table(conn)

        print("\n-- CREATE")
        new_id = create_tarefa(conn, "Comprar material", "Tinta, pincéis e rolos", "pendente")
        print("Inserido id:", new_id)

        print("\n-- READ (todas)")
        all_rows = get_all(conn)
        pp.pprint(all_rows)

        print("\n-- READ (por id)")
        item = get_by_id(conn, new_id)
        pp.pprint(item)

        print("\n-- UPDATE")
        updated = update_tarefa(conn, new_id, titulo="Comprar material de pintura", status="em_progresso")
        print("Atualizado:")
        pp.pprint(updated)

        print("\n-- DELETE")
        deleted = delete_tarefa(conn, new_id)
        print("Removido (antes da remoção):")
        pp.pprint(deleted)

        print("\n-- READ (final)")
        pp.pprint(get_all(conn))

    finally:
        conn.close()


if __name__ == '__main__':
    main()
