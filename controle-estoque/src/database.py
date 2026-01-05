import sqlite3
import os


DB_PATH = os.path.join("database", "estoque.db")


def conectar():
    return sqlite3.connect(DB_PATH)


def criar_tabela():
    os.makedirs("database", exist_ok=True)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    

