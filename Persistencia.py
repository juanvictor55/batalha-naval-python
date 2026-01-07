def salvar_score(nome, pontos):
    with open("ranking.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{pontos}\n")

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

    print('\n==== Melhores Pontações ====\n'
          '   Nome    # Jogadas')
    for posicao, (nome, pontos) in enumerate(ranking[:10], start=1):
        print(f"{posicao:<3}{nome:<12}{pontos}")
