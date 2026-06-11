from estoque import (
    cadastrar_produto,
    listar_produtos,
    listar_por_categoria,
    estoque_baixo
)


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
        3
    )

    cadastrar_produto(
        produtos,
        1003,
        "Monitor",
        "Monitores",
        899.90,
        2
    )

    print("=== TODOS OS PRODUTOS ===\n")

    for produto in listar_produtos(produtos):
        produto.exibir()
        print()

    print("=== PERIFÉRICOS ===\n")

    for produto in listar_por_categoria(produtos, "Periféricos"):
        produto.exibir()
        print()

    print("=== ESTOQUE BAIXO (< 5) ===\n")

    for produto in estoque_baixo(produtos, 5):
        produto.exibir()
        print()


if __name__ == "__main__":
    main()