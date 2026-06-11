from estoque import cadastrar_produto, buscar_por_codigo


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

    cadastrar_produto(
        produtos,
        1002,
        "Teclado Mecânico",
        "Periféricos",
        150.00,
        8
    )

    cadastrar_produto(
        produtos,
        1003,
        "Headset",
        "Periféricos",
        199.90,
        5
    )

    produto = buscar_por_codigo(produtos, 1002)

    if produto:
        produto.exibir()
    else:
        print("Produto não encontrado.")


if __name__ == "__main__":
    main()