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

    posicao = 0

    while (
        posicao < len(produtos)
        and produtos[posicao].codigo < codigo
    ):
        posicao += 1

    produtos.insert(posicao, novo_produto)

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

def editar_produto(produtos, codigo, nome, categoria, preco, quantidade):
    produto = buscar_por_codigo(produtos, codigo)

    if produto is None:
        return False

    produto.nome = nome
    produto.categoria = categoria
    produto.preco = preco
    produto.quantidade = quantidade

    return True

def remover_produto(produtos, codigo):
    produto = buscar_por_codigo(produtos, codigo)

    if produto is None:
        return False

    produtos.remove(produto)

    return True

def buscar_por_nome(produtos, nome):
    encontrados = []

    for produto in produtos:
        if nome.lower() in produto.nome.lower():
            encontrados.append(produto)

    return encontrados

def registrar_venda(produtos, codigo, quantidade_vendida):
    produto = buscar_por_codigo(produtos, codigo)

    if produto is None:
        return "nao_encontrado"

    if quantidade_vendida > produto.quantidade:
        return "estoque_insuficiente"

    produto.quantidade -= quantidade_vendida

    return "sucesso"

def listar_produtos(produtos):
    return produtos


def listar_por_categoria(produtos, categoria):
    encontrados = []

    for produto in produtos:
        if produto.categoria.lower() == categoria.lower():
            encontrados.append(produto)

    return encontrados


def estoque_baixo(produtos, limite):
    encontrados = []

    for produto in produtos:
        if produto.quantidade < limite:
            encontrados.append(produto)

    return encontrados