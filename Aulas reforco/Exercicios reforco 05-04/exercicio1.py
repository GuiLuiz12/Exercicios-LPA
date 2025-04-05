def menu():
    print("\n=== MENU ===")
    print("1 - Adicionar produto")
    print("2 - Consultar produto")
    print("3 - Sair")

def addProduto(estoque):
    nomeProduto = input("\nDigite o nome do produto: ")
    try:
        quantidade = int(input("Digite a quantidade: "))

        if nomeProduto in estoque:
            estoque[nomeProduto] += quantidade
            print(f"\nQuantidade atualizada! Novo total: {estoque[nomeProduto]}")
        else:
            estoque[nomeProduto] = quantidade
            print(f"\nProduto adicionado!")

    except ValueError:
        print("\nErro: Quantidade deve ser um número inteiro!")

def consultarProduto(estoque):
    nomeProduto = input("\nDigite o nome do produto para consulta: ")

    if nomeProduto in estoque:
        print(f"\nQuantidade disponível: {estoque[nomeProduto]}")
    else:
        print("\nProduto não encontrado.")

def main():
    estoque = {}
    opcao = 0

    while opcao != 3:
        menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                addProduto(estoque)
            elif opcao == 2:
                consultarProduto(estoque)
            elif opcao == 3:
                print("\nSaindo do sistema...")
            else:
                print("\nOpção inválida! Tente novamente.")

        except ValueError:
            print("\nErro: Opção deve ser um número inteiro!")
            opcao = 0

if __name__ == "__main__":
    main()