from database import criar_tabela
from database import cadastrar_produto, listar_produtos


def main():
    criar_tabela()
    print("Tabela de produtos criada com sucesso!")


if __name__ == "__main__":
    main()


def menu():
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
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
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opcão invalida!")
        if __name__ == "__main__":
            main()