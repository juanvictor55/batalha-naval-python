import string

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
