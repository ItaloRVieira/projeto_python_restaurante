from modelos.restaurantes import Restaurantes
from modelos.menu import Menu
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.pratos import Prato

restaurante_coxinha = Restaurantes('Coxinha', 'Salgados')
restaurante_coxinha.receber_avaliacao('Italo', 5)
restaurante_coxinha.receber_avaliacao('Sofia', 4)
bebida_suco_abacaxi = Bebida('Suco de abacaxi', 5.0, 'grande')
bebida_suco_abacaxi.aplicar_desconto()
prato_coxinha_catupiry = Prato('Coxinha de frango', 4.50, 'Frita na hora')
restaurante_coxinha.adicionar_ao_cardapio(bebida_suco_abacaxi)
restaurante_coxinha.adicionar_ao_cardapio(prato_coxinha_catupiry)
restaurante_pasteis = Restaurantes('pasteis', 'pastelaria')
restaurante_pasteis.alterar_status()

    
def main():
    #restaurante_coxinha.exibir_cardapio
    Menu.menu_inicial()
    Menu.opcao_menu()

if __name__ == '__main__':
    main()