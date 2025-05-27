class Carrinho:
    def __init__(self, item, quantidade):
        self.item = item
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.item.nome} | {self.item.preco} | {self.quantidade}'
    

    