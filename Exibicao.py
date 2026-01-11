import string

def criar_tabuleiro_visual(linhas, colunas):
    tab_visual = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append("\u25A0")
        tab_visual.append(linha)
    return tab_visual

def mostrar_tabuleiro(tab_visual):
    linhas = len(tab_visual)
    colunas = len(tab_visual[0])
    letras = string.ascii_uppercase

    # Formatando linha de cabeçalho:
    print('\n     ',end='')
    for coluna in range(1, colunas + 1):
        print(coluna, end=" ")
    print()

    # Aparência do tabuleiro
    for i in range(linhas):
        print(f"{letras[i]} |  ", end="")
        for j in range(colunas):
            print(tab_visual[i][j], end=" ")
        print()


def mensagem_menu():
    print("""
╔════════════════════════════════════════════╗
║        BEM-VINDO AO BATALHA NAVAL!         ║
╚════════════════════════════════════════════╝

1 - Jogar
2 - Ver Melhores Pontuações
3 - Sair""")

def exibir_instrucoes_jogo():
    print("""
╔════════════════════════════════════════════╗
║        BEM-VINDO AO BATALHA NAVAL!         ║
╚════════════════════════════════════════════╝

Objetivo:
- Para vencer o jogo, você deve afundar todas as embarcações inimigas.
- No total, são 5 navios e 3 submarinos.

Legenda do tabuleiro:
_  → Água
X  → Embarcação afundada
⌖  → Submarino parcialmente atingido
■  → Posição ainda não explorada

Como jogar:
- Digite a linha e a coluna para realizar uma jogada.
- Exemplo: A 2

Boa sorte, comandante!
""")

def msg_posicao_repetida():
    print('''
╔══════════════════════════════╗
║  Posição repetida!           ║
║  Escolha outro alvo.         ║
╚══════════════════════════════╝''')

def msg_agua():
    print('''
╔══════════════════════════════╗
║   ÁGUA!!!!                   ║
╚══════════════════════════════╝''')

def msg_acerto():
    print('''
╔══════════════════════════════╗
║   Acertou uma embarcação!    ║
╚══════════════════════════════╝''')

def msg_formato_invalido():
    print('''
╔══════════════════════════════╗
║  Formato inválido            ║
╚══════════════════════════════╝''')
