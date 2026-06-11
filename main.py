from estoque import (
    cadastrar_produto,
    buscar_por_nome
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
        "Mouse Sem Fio",
        "Periféricos",
        120.00,
        10
    )

    cadastrar_produto(
        produtos,
        1003,
        "Teclado Mecânico",
        "Periféricos",
        150.00,
        8
    )

    resultados = buscar_por_nome(produtos, "mouse")

    print(f"Encontrados: {len(resultados)}\n")

    for produto in resultados:
        produto.exibir()
        print()


if __name__ == "__main__":
    main()