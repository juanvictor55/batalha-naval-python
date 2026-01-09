from Tabuleiro import Tabuleiro
from Exibicao import *
from Persistencia import *
import string

def menu_principal():
    # Exibe o menu principal do jogo e gerencia a escolha do usuário.
    mensagem_menu = """
╔════════════════════════════════════════════╗
║        BEM-VINDO AO BATALHA NAVAL!         ║
╚════════════════════════════════════════════╝

1 - Jogar
2 - Ver Melhores Pontuações
3 - Sair
Escolha uma opção: """

    while True:
        opcao = input(mensagem_menu)

        if opcao == '1':
            iniciar_jogo()
            break
        elif opcao == '2':
            mostrar_ranking_formatado()
        elif opcao == '3':
            print('Finalizando programa...')
            break
        else:
            print("\n==> Opção inválida. Tente novamente.")

