from estoque import (
    cadastrar_produto,
    editar_produto,
    remover_produto,
    buscar_por_codigo,
    buscar_por_nome,
    registrar_venda,
    listar_produtos,
    listar_por_categoria,
    estoque_baixo
)

from arquivos import salvar_produtos, carregar_produtos


def cabecalho(titulo):
    print("\n" + "=" * 60)
    print(titulo.center(60))
    print("=" * 60)


def menu():
    cabecalho("SISTEMA DE ESTOQUE E VENDAS")

    print("[1] Cadastrar Produto")
    print("[2] Editar Produto")
    print("[3] Remover Produto")

    print("\n---------------- BUSCAS ----------------")

    print("[4] Buscar por Código")
    print("[5] Buscar por Nome")

    print("\n---------------- VENDAS ----------------")

    print("[6] Registrar Venda")

    print("\n-------------- RELATÓRIOS --------------")

    print("[7] Estoque Geral")
    print("[8] Produtos por Categoria")
    print("[9] Estoque Baixo")

    print("\n--------------- SISTEMA ----------------")

    print("[0] Salvar e Sair")

    print("=" * 60)


def exibir_lista(produtos):
    if len(produtos) == 0:
        print("\nNenhum produto encontrado.")
        return

    for produto in produtos:
        produto.exibir()
        print("-" * 60)


def main():
    produtos = carregar_produtos()

    while True:
        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cabecalho("CADASTRAR PRODUTO")

            codigo = int(input("Código: "))
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))

            sucesso = cadastrar_produto(
                produtos,
                codigo,
                nome,
                categoria,
                preco,
                quantidade
            )

            if sucesso:
                print("\n✓ Produto cadastrado com sucesso.")
            else:
                print("\n✗ Já existe um produto com esse código.")

        elif opcao == "2":
            cabecalho("EDITAR PRODUTO")

            codigo = int(input("Código do produto: "))

            nome = input("Novo nome: ")
            categoria = input("Nova categoria: ")
            preco = float(input("Novo preço: "))
            quantidade = int(input("Nova quantidade: "))

            sucesso = editar_produto(
                produtos,
                codigo,
                nome,
                categoria,
                preco,
                quantidade
            )

            if sucesso:
                print("\n✓ Produto editado com sucesso.")
            else:
                print("\n✗ Produto não encontrado.")

        elif opcao == "3":
            cabecalho("REMOVER PRODUTO")

            codigo = int(input("Código do produto: "))

            sucesso = remover_produto(produtos, codigo)

            if sucesso:
                print("\n✓ Produto removido com sucesso.")
            else:
                print("\n✗ Produto não encontrado.")

        elif opcao == "4":
            cabecalho("BUSCAR POR CÓDIGO")

            codigo = int(input("Código: "))

            produto = buscar_por_codigo(produtos, codigo)

            if produto:
                print()
                produto.exibir()
            else:
                print("\n✗ Produto não encontrado.")

        elif opcao == "5":
            cabecalho("BUSCAR POR NOME")

            nome = input("Nome: ")

            encontrados = buscar_por_nome(produtos, nome)

            exibir_lista(encontrados)

        elif opcao == "6":
            cabecalho("REGISTRAR VENDA")

            codigo = int(input("Código do produto: "))
            quantidade = int(input("Quantidade vendida: "))

            sucesso = registrar_venda(
                produtos,
                codigo,
                quantidade
            )

            if sucesso:
                print("\n✓ Venda registrada com sucesso.")
            else:
                print("\n✗ Venda não realizada.")

        elif opcao == "7":
            cabecalho("ESTOQUE GERAL")

            exibir_lista(listar_produtos(produtos))

        elif opcao == "8":
            cabecalho("PRODUTOS POR CATEGORIA")

            categoria = input("Categoria: ")

            encontrados = listar_por_categoria(
                produtos,
                categoria
            )

            exibir_lista(encontrados)

        elif opcao == "9":
            cabecalho("ESTOQUE BAIXO")

            limite = int(input("Limite de estoque: "))

            encontrados = estoque_baixo(
                produtos,
                limite
            )

            exibir_lista(encontrados)

        elif opcao == "0":
            salvar_produtos(produtos)

            cabecalho("ENCERRANDO SISTEMA")
            print("Dados salvos com sucesso.")

            break

        else:
            print("\nOpção inválida.")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()