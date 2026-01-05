from database import criar_tabela
from estoque import (
    cadastrar_produto,
    listar_produtos,
    atualizar_produto,
    remover_produto
)


def menu():
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("0 - Sair")


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("❌ Digite um número inteiro válido.")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Digite um número válido.")


def main():
    criar_tabela()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = ler_int("Quantidade: ")
            preco = ler_float("Preço: ")
            cadastrar_produto(nome, quantidade, preco)

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            id_produto = ler_int("ID do produto: ")
            quantidade = ler_int("Nova quantidade: ")
            preco = ler_float("Novo preço: ")
            atualizar_produto(id_produto, quantidade, preco)

        elif opcao == "4":
            id_produto = ler_int("ID do produto: ")
            remover_produto(id_produto)

        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()
