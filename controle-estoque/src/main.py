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
    print("3 - Atualizar produtos")
    print("4 - Remover produtos")
    print("0 - Sair")


def main():
    criar_tabela()
    while True:
        menu()
        opcao = input("Escolha um opção: ")
        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            cadastrar_produto(nome, quantidade, preco)
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Nova quantidade: "))
            preco = float(input("Novo preço: "))
            atualizar_produto(id_produto, quantidade, preco)

        elif opcao == "4":
            id_produto = int(input("ID do produto: "))
            remover_produto(id_produto)
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opcão invalida!")
        if __name__ == "__main__":
            main()