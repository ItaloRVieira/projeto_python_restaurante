from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    
    bebidas = []
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        Bebida.bebidas.append(self)

   # def __str__(self):
    #    return f'{self.nome} | {self._preco} | {self.tamanho}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)