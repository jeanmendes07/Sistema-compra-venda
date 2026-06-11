from produto import Produto


def codigo_existe(produtos, codigo):
    for produto in produtos:
        if produto.codigo == codigo:
            return True

    return False


def cadastrar_produto(produtos, codigo, nome, categoria, preco, quantidade):
    if codigo_existe(produtos, codigo):
        return False

    novo_produto = Produto(
        codigo,
        nome,
        categoria,
        preco,
        quantidade
    )

    produtos.append(novo_produto)

    return True