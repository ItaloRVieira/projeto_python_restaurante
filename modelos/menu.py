from modelos.restaurantes import Restaurantes
class Menu:

    def menu_inicial():
        print('Selecione uma opção:\n1. Cadastrar Restaurante\n2. Listar restaurantes\n3. Alterar Status\n4. Avaliar Restaurante\n5. Sair')
    
    def opcao_menu():
        try:
            escolha = int(input('Escolha uma opção válida: '))
            if escolha == 1:
                Restaurantes.cadastrar_restaurante()
                Menu.retornar_ao_menu()
            elif escolha == 2:
                Restaurantes.listar_restaurantes()
                Menu.retornar_ao_menu()
            elif escolha == 3:
                Restaurantes.ativar_desativar_restaurante()
                Menu.retornar_ao_menu()
            elif escolha == 4:
                Restaurantes.avaliar_restaurante()
                Menu.retornar_ao_menu()
            elif escolha == 5:
                Restaurantes.sair()
        except ValueError:
            print('Opção inválida, tente novamente.')
            Menu.opcao_menu()
    
    def retornar_ao_menu():
        Menu.menu_inicial()
        Menu.opcao_menu()