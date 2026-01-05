from database import conectar


def cadastrar_produto(nome, quantidade, preco):
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
            (nome, quantidade, preco)
        )

        conn.commit()
        print("✅ Produto cadastrado com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao cadastrar produto: {e}")

    finally:
        conn.close()


def listar_produtos():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

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

    except Exception as e:
        print(f"❌ Erro ao listar produtos: {e}")

    finally:
        conn.close()


def atualizar_produto(id_produto, quantidade, preco):
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE produtos SET quantidade = ?, preco = ? WHERE id = ?",
            (quantidade, preco, id_produto)
        )

        if cursor.rowcount == 0:
            print("⚠️ Produto não encontrado.")
        else:
            print("🔄 Produto atualizado com sucesso!")

        conn.commit()

    except Exception as e:
        print(f"❌ Erro ao atualizar produto: {e}")

    finally:
        conn.close()


def remover_produto(id_produto):
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))

        if cursor.rowcount == 0:
            print("⚠️ Produto não encontrado.")
        else:
            print("🗑️ Produto removido com sucesso!")

        conn.commit()

    except Exception as e:
        print(f"❌ Erro ao remover produto: {e}")

    finally:
        conn.close()
