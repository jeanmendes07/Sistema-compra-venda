from produto import Produto


def main():
    produto = Produto(
        1001,
        "Mouse Gamer",
        "Periféricos",
        89.90,
        15
    )

    produto.exibir()


if __name__ == "__main__":
    main()