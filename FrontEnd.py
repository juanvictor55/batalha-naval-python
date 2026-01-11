from Tabuleiro import Tabuleiro
from Exibicao import *
from Persistencia import *
import string

def menu_principal():
    # Exibe o menu principal do jogo e gerencia a escolha do usuário.
    while True:
        mensagem_menu()
        opcao = input('Escolha uma opção: ')

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

def iniciar_jogo():
    num_linhas = 6
    num_colunas = 6
    num_navios = 5
    num_submarinos = 3
    
    tabuleiro = Tabuleiro(num_linhas, num_colunas, num_navios, num_submarinos)
    linhas, colunas = tabuleiro.getDimensoes()
    tab_visual = criar_tabuleiro_visual(linhas, colunas)

    placar_jogadas = 0
    navios_afundados = 0
    submarinos_afundados  = 0
    jogadas_feitas = set()

    total_navios  = tabuleiro.numNavios 
    total_submarinos  = tabuleiro.numSubmarinos
    letras = string.ascii_uppercase

    # Mostra instruções antes do loop principal iniciar
    exibir_instrucoes_jogo()
    input("Pressione Enter para começar a jogar...")

    # Loop principal:
    while True:
        mostrar_tabuleiro(tab_visual)

        # Informa sobre estado atual:
        print(
            f'\nJogadas até agora: {placar_jogadas}\n'
            f'Afundados até agora: ' 
            f'Navios {navios_afundados} de {total_navios} | '
            f'Submarinos {submarinos_afundados} de {total_submarinos}\n'
            f'Para desistir digite: -1'
            )
        
        # Captura nova jogada:
        posicao = input('Digite a linha e coluna (ex.: A 2): ').upper()
        
        # Jogador desistiu:
        if posicao == '-1':
            print('\nFinalizando jogada')
            return menu_principal()

        # Validando formato da jogada
        try:
            # Convertendo o input em índices numéricos
            linha_str, coluna_str = posicao.split()
            linha_idx = letras.index(linha_str)
            coluna_idx = int(coluna_str) - 1
            
            # Verificando se a jogada é repetida
            if (linha_idx, coluna_idx) in jogadas_feitas:
                msg_posicao_repetida()
                continue

            # Verificando se o input está dentro do range do tabuleiro
            if 0 <= linha_idx < linhas and 0 <= coluna_idx < colunas:
                jogadas_feitas.add((linha_idx, coluna_idx))
                placar_jogadas += 1

                # Se sim: Verifica conteúdo da jogada
                valor_jogada = tabuleiro.getPosicao(linha_idx, coluna_idx)
                if valor_jogada == 0:
                    msg_agua()
                    tab_visual[linha_idx][coluna_idx] = "_"
                    continue
                elif valor_jogada == 1:
                    msg_acerto()

                    # Marcando no tabuleiro o acerto no navio:
                    barco_atingido = tabuleiro.indiceReversoPosicoesBarcos[(linha_idx, coluna_idx)]
                    tabuleiro.setPosicao(linha_idx, coluna_idx, 0)
                    tabuleiro.posicaoEmbarcacoes[barco_atingido][(linha_idx, coluna_idx)] = 0
                    tab_visual[linha_idx][coluna_idx] = "\u2316"

                    # Verificando se todas as partes do navio foram acertadas:
                    todos_atingidos = True
                    for valor in tabuleiro.posicaoEmbarcacoes[barco_atingido].values():
                        if valor == 1:
                            todos_atingidos = False
                            break

                    # Atualizando o score de barcos:
                    if todos_atingidos:
                        if barco_atingido[0] == 'b':
                            navios_afundados += 1
                        elif barco_atingido[0] == 's':
                            submarinos_afundados += 1

                        # Marcando 'X' nos barcos afundados no tabuleiro visual
                        for (i, j) in tabuleiro.posicaoEmbarcacoes[barco_atingido]:
                            tab_visual[i][j] = "X"
                    
                    # Verificando se o usuário ganhou:
                    if navios_afundados == total_navios and submarinos_afundados == total_submarinos:
                        mostrar_tabuleiro(tab_visual)
                        print("\n****** Parabéns! Você afundou todas as embarcações! ******\n")
                        nome_jogador = input("Digite seu nome: ")
                        salvar_score(nome_jogador, placar_jogadas)
                        mostrar_ranking_formatado()
                        return menu_principal()

            # Se não: O usuário digitou um formato maior que o tabuleiro 
            else:
                msg_formato_invalido()
                continue

        # O usuário digitou qualquer formato inválido
        except (ValueError, IndexError):
            msg_formato_invalido()
            continue    
