def salvar_score(nome, pontos):
    arquivo = open("ranking.txt", 'a')
    arquivo.write(f'{nome},{pontos}\n')
    arquivo.close()

def ler_ranking():
    ranking = []
    try:
        with open("ranking.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, pontos = linha.strip().split(",")
                ranking.append((nome, int(pontos)))
    except FileNotFoundError:
        return []
    return ranking
    
def mostrar_ranking_formatado():
    ranking = ler_ranking()
    if not ranking:
        print("\n==== Ranking Vazio ====")
        return

    ranking.sort(key=lambda item: item[1])
    posicao = 1

    print('\n==== Melhores Pontações ====\n'
          '   Nome    # Jogadas')
    for nome, pontos in ranking:
        print(f'{posicao:<3}{nome:<12}{pontos}')
        posicao += 1

