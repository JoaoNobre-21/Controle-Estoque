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


def cadastrar_produto(nome, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (?, ?, ?)
    """, (nome, quantidade, preco))
    conn.commit()
    conn.close()
    print(f"✅ Produto '{nome}' cadastrado com sucesso!")
    conn.commit()
    conn.close()


def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    conn.close()

    if not produtos:
        print("⚠️ Nenhum produto cadastrado.")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")
    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Nome: {produto[1]} | "
            f"Quantidade: {produto[2]} | "
            f"Preço: R$ {produto[3]:.2f}"
        )
        conn.commit()
        conn.close()