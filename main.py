from estoque import cadastrar_produto


def main():
    produtos = []

    resultado = cadastrar_produto(
        produtos,
        1001,
        "Mouse Gamer",
        "Periféricos",
        89.90,
        15
    )

    if resultado:
        print("Produto cadastrado com sucesso.")
    else:
        print("Produto já existe.")

    resultado = cadastrar_produto(
        produtos,
        1001,
        "Teclado",
        "Periféricos",
        120.00,
        10
    )

    if resultado:
        print("Produto cadastrado com sucesso.")
    else:
        print("Produto já existe.")


if __name__ == "__main__":
    main()