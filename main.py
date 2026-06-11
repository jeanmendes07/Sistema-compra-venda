from estoque import (
    cadastrar_produto,
    registrar_venda,
    buscar_por_codigo
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

    sucesso = registrar_venda(
        produtos,
        1001,
        3
    )

    if sucesso:
        print("Venda registrada com sucesso.")
    else:
        print("Não foi possível registrar a venda.")

    produto = buscar_por_codigo(produtos, 1001)

    if produto:
        print(f"Estoque restante: {produto.quantidade}")


if __name__ == "__main__":
    main()