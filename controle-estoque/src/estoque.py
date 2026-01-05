from database import conectar


def cadastrar_produto(nome, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, quantidade, preco) values ( ?, ?, ?)",
        (nome, quantidade, preco)
    )
    conn.commit()
    conn.close()
    print("Produto cadastrado com sucesso!")


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
