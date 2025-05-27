from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):

    pratos = []
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
        Prato.pratos.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._preco} | {self.descricao}'
    
    @classmethod
    def listar_pratos(cls):
        for prato in cls.pratos:
            print(f'{prato._nome} | {prato._preco} | {prato.descricao}') 

    def cadastrar_prato(self):
        _nome = input('Digite o nome do prato: ')
        _preco = float(input('Digite o preco do produto: '))
        descricao = input('Informe a descrição do seu prato: ')
        Prato(_nome, _preco, descricao)

    def menu_restaurante(self):
        pass

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)


