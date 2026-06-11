class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def exibir(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")