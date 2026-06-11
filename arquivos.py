import json

from produto import Produto


def salvar_produtos(produtos, nome_arquivo="dados.json"):
    dados = []

    for produto in produtos:
        dados.append(produto.para_dicionario())

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def carregar_produtos(nome_arquivo="dados.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        return []

    produtos = []

    for item in dados:
        produto = Produto(
            item["codigo"],
            item["nome"],
            item["categoria"],
            item["preco"],
            item["quantidade"]
        )

        produtos.append(produto)

    return produtos