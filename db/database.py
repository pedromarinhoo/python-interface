import sqlite3 as sql

DB_NAME = "crud.db"

def conectar():
    return sql.connect(DB_NAME)

def criarTabela():
    sql_clientes = '''
        CREATE TABLE IF NOT EXISTS Cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR (100) NOT NULL,
        telefone VARCHAR (12)
        );
    '''
    conn = conectar()
    cur = conn.cursor()
    cur.execute(sql_clientes)
    conn.commit()
    conn.close()

def inserirCliente(nome, telefone):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO Cliente (nome, telefone) VALUES (?, ?)", (nome, telefone))
    conn.commit()
    conn.close()

def listarClientes():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cliente")
    rows = cur.fetchall()
    conn.close()
    return rows

def excluirCliente(id_cliente):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM Cliente WHERE id=?", (id_cliente,))
    conn.commit()
    conn.close()
