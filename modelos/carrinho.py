class Carrinho:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f'{self.nome} | {self.item.preco} | {self.quantidade}'
    

    