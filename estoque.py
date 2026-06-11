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

def buscar_por_codigo(produtos, codigo):
    inicio = 0
    fim = len(produtos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if produtos[meio].codigo == codigo:
            return produtos[meio]

        elif produtos[meio].codigo < codigo:
            inicio = meio + 1

        else:
            fim = meio - 1

    return None