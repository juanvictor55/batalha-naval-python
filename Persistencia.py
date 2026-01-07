def salvar_score(nome, pontos):
    arquivo = open("ranking.txt", 'a')
    arquivo.write(f'{nome},{pontos}\n')
    arquivo.close()

def ler_ranking():
    ranking = []
    try:
        arquivo = open("ranking.txt")
        conteudo = arquivo.readlines()
        arquivo.close()

        for linha in conteudo:
            nome, pontos = linha.strip().split(',')
            ranking.append((nome,int(pontos)))
        return ranking
    
    except FileNotFoundError:
        pass

def mostrar_ranking_formatado():
    ranking = ler_ranking()
    if not ranking:
        print("\n==== Ranking Vazio ====")
        return

    ranking.sort(key=lambda x: x[1])
    posicao = 1

    print('\n==== Melhores Pontações ====\n'
          '   Nome    # Jogadas')
    for nome, pontos in ranking:
        print(f'{posicao:<3}{nome:<12}{pontos}')
        posicao += 1
