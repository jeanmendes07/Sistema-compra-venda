from estoque import cadastrar_produto
from arquivos import salvar_produtos, carregar_produtos


def main():
    produtos = carregar_produtos()

    if len(produtos) == 0:
        cadastrar_produto(
            produtos,
            1001,
            "Mouse Gamer",
            "Periféricos",
            89.90,
            15
        )

        salvar_produtos(produtos)

        print("Produto salvo no JSON.")

    else:
        print("Produtos carregados:")

        for produto in produtos:
            produto.exibir()


if __name__ == "__main__":
    main()