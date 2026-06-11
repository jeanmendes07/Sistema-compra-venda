from estoque import cadastrar_produto


def main():
    produtos = []

    cadastrar_produto(
        produtos,
        1003,
        "Headset",
        "Periféricos",
        199.90,
        5
    )

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

    for produto in produtos:
        print(produto.codigo)


if __name__ == "__main__":
    main()