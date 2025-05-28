from modelos.avaliacoes import Avaliacoes
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.carrinho import Carrinho


class Restaurantes:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        self._carrinho = []
        Restaurantes.restaurantes.append(self)
        

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f' {'Nº'.ljust(4)} | {('Nome do Restaurante'.ljust(25))} | {'Categoria do Restaurante '} | {'Status'.ljust(10)} | {'Quantidade avaliações'.ljust(20)} | {'Media'}')
        for i, restaurante in enumerate(cls.restaurantes, start=1):
            print(
                f'{str(i).ljust(5)} | {restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(10)} | {str(restaurante.quantidade_avaliacoes).ljust(21)} | '
                f'{str(restaurante.media) if restaurante.quantidade_avaliacoes > 0 else "Nenhuma avaliação"}')
        
        Restaurantes.escolher_restaurante(cls)
                    

    @property
    def ativo(self):
        return 'ATIVO' if self._ativo else 'DESATIVADO'

    def alterar_status(self):
        self._ativo = not self._ativo

   
    @classmethod
    def ativar_desativar_restaurante(cls):
        from modelos.menu import Menu
        nome = input('Digite o nome do restaurante que deseja alterar o status: ').title()
        for restaurante in cls.restaurantes:
            if restaurante.nome == nome:
                restaurante.alterar_status()
                print(f'O restaurante {restaurante.nome} foi ativado com sucesso' if restaurante._ativo else f'O restaurante {restaurante.nome} foi desativado')
                Menu.retornar_ao_menu()
                return

        print('Nome incorreto')
        Menu.retornar_ao_menu()

        
    
    @property
    def quantidade_avaliacoes(self):
        return len(self._avaliacao)
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacoes(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @classmethod
    def avaliar_restaurante(cls):
        nome = input('Digite o nome do restaurante que deseja avaliar: ').title()
        for restaurante in cls.restaurantes:
            if restaurante.nome == nome:
                cliente = input('Informe seu nome: ')
                nota = int(input('Informe uma nota de 1 a 5: '))
                if 1 <= nota <= 5:
                    print(f'Avaliação de {nota} registrada para restaurante {nome}')
                    avaliacao = Avaliacoes(cliente, nota)
                    restaurante._avaliacao.append(avaliacao)

                else: print('A avaliação deve conter entre 1 e 5')
    
    @property
    def media(self):
        if not self._avaliacao:
            return 0
        soma = sum(avaliacao._notas for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media

    def cadastrar_restaurante():
        print('Infome os dados do restaurante que deseja cadastrar')
        nome = input('Informe o nome do restaurante: ').title()
        categoria = input('Agora informe a categoria do restaurante: ').title()
        Restaurantes(nome, categoria)

    @staticmethod
    def sair():
        import sys, os
        print('Encerrando o sistema')
        os.system('cls')
        sys.exit()

    @staticmethod   
    def escolher_restaurante(cls):
        try:
            numero = int(input(f'Selecione o restaurante que deseja acessar: '))
        except ValueError:
            print('Insira um número válido')
            return
        if 1 <= numero <= len(cls.restaurantes):
            restaurante = cls.restaurantes[numero - 1]
            from modelos.cardapio.pratos import Prato
            Prato.menu_restaurante(restaurante)
            print(f"Você acessou o menu do restaurante: {restaurante.nome}.\n")
            Restaurantes.exibir_cardapio(restaurante)
        else:
            print("Número inválido. Por favor, selecione um número válido.")

    def adicionar_ao_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self.nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = (f'{i}. Nome: {item._nome.ljust(25)} | R$ {str(item._preco).ljust(6)} | Descrição: {item.descricao.ljust(30)}\n')
                print(mensagem_prato)
            elif hasattr(item, 'tamanho'):
                mensagem_bebida = (f'{i}. Nome: {item._nome.ljust(25)} | R$ {str(item._preco).ljust(6)} | Tamanho: {item.tamanho.ljust(30)}\n')
                print(mensagem_bebida)
        Restaurantes.selecionar_item_cardapio(self)
                    
    def adicionar_ao_carrinho(self, item, quantidade, preco):
        if isinstance(item, ItemCardapio):
            carrinho_item = Carrinho(item._nome, quantidade, preco)
            self._carrinho.append(carrinho_item)
            print(f'{quantidade} {item._nome} adicionado ao carrinho.\n\n')
        else:
            print('Item inválido para o carrinho.')
        Restaurantes.exibir_cardapio(self)
    
    def lista_carrinho(self):
        if not self._carrinho:
            print('Seu carrinho está vazio.')
            Restaurantes.exibir_cardapio(self)
        else: 
            print(f'{'Item'.ljust(20)} | {'Quantidade'.ljust(12)} | {'Preço'.ljust(10)} | {'Total'.ljust(10)}')
            for item in self._carrinho:
                print(f'{item.nome.ljust(20)} | {str(item.quantidade).ljust(12)} | {str(item.preco).ljust(10)} | {item.preco * item.quantidade}')
            print(f'Total do carrinho: R$ {sum(item.preco * item.quantidade for item in self._carrinho)}')  
        
    
    def selecionar_item_cardapio(self):
        item = int(input('Informe o número do item que deseja adicionar ao carrinho ou pressione 0 para ir ao carrinho: '))
        if item == 0:
            self.lista_carrinho()
        try:
            if 1 <= item <= len(self._cardapio):
                item_cardapio = self._cardapio[item - 1]
                nome = item_cardapio._nome
                preco = item_cardapio._preco
                quantidade = int(input('Informe a quantidade que deseja adicionar ao carrinho: '))
                
                encontrado = False
                for produtos in self._carrinho:
                    if produtos.nome == nome:
                        produtos.quantidade += quantidade
                        encontrado = True
                        break
                if not encontrado:
                    self.adicionar_ao_carrinho(item_cardapio, quantidade, preco)
                    return f'Item {item_cardapio._nome} adicionado ao carrinho com sucesso.'
                Restaurantes.exibir_cardapio(self)
                        
        except ValueError:
                print('Item não encontrado no cardápio.')
                Restaurantes.exibir_cardapio(self)
                return 'Tente novamente.'


