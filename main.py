from estoque import cadastrar_produto, editar_produto, buscar_por_codigo


def main():
    produtos = []

    cadastrar_produto(
        produtos,
        1001,
        "Mouse Gamer",
        "Periféricos",
        89.90,
        15
    )

    sucesso = editar_produto(
        produtos,
        1001,
        "Mouse Gamer RGB",
        "Periféricos",
        109.90,
        20
    )

    if sucesso:
        print("Produto editado com sucesso.")
    else:
        print("Produto não encontrado.")

    produto = buscar_por_codigo(produtos, 1001)

    if produto:
        produto.exibir()


if __name__ == "__main__":
    main()