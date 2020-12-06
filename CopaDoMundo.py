selecoes = []
dic = {}
for i in range(16):
    selecao = input()
    selecoes.append(selecao)
    dic[selecao] = {
        "partidas": 0,
        "vitorias": 0,
        "derrotas": 0,
        "penaltis": 0,
        "normal": 0,
        "marcados": 0,
        "sofridos": 0
    }

# Leitura das partidas e processamento dos dados

for i in range(16):
    jogo = str(input())
    valores = jogo.split(' ')
    primeiro_time = valores[0]
    segundo_time = valores[4]



    if len(valores) > 5:
        segundo_time = valores[7]


        # Partida Normal (Ja tira um pq entrou na condição dos penaltis)
        dic[segundo_time]['normal'] -= 1
        dic[primeiro_time]['normal'] -= 1

        # Penaltis
        dic[primeiro_time]['penaltis'] += 1
        dic[segundo_time]['penaltis'] += 1

        # Tratamento da variavel
        gol_primeiro_time = int(valores[4].replace('(', ''))
        gol_segundo_time = int(valores[6].replace(')', ''))


        if gol_primeiro_time > gol_segundo_time:
            dic[primeiro_time]['vitorias'] += 1
            dic[segundo_time]['derrotas'] += 1
        else:
            dic[segundo_time]['vitorias'] += 1
            dic[primeiro_time]['derrotas'] += 1

    gol_primeiro_time = int(valores[1])
    gol_segundo_time = int(valores[3])


    # Primeiro time Normal
    dic[primeiro_time]['marcados'] += gol_primeiro_time
    dic[primeiro_time]['sofridos'] += gol_segundo_time

    # Segundo time Normal
    dic[segundo_time]['marcados'] += gol_segundo_time
    dic[segundo_time]['sofridos'] += gol_primeiro_time

    # Partida
    dic[segundo_time]['partidas'] += 1
    dic[primeiro_time]['partidas'] += 1

    # Partida Normal
    dic[segundo_time]['normal'] += 1
    dic[primeiro_time]['normal'] += 1

    # Vitoria e Derrota
    # Nunca entrara nessa condiçao caso seja um empate
    if int(gol_segundo_time > gol_primeiro_time):
        dic[segundo_time]['vitorias'] += 1
        dic[primeiro_time]['derrotas'] += 1
    elif int(gol_primeiro_time > gol_segundo_time):
        dic[primeiro_time]['vitorias'] += 1
        dic[segundo_time]['derrotas'] += 1

campeao = ''
for time in dic.keys():
    if dic[time]['derrotas'] == 0:
        campeao = time

# Saída de dados

for selecao in selecoes:
    print("-" * 50)
    print("Pais:", selecao)
    print("Partidas:", dic[selecao]["partidas"])
    print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
    print("Partidas decicidas nos penaltis:", dic[selecao]["penaltis"])
    print("Vitorias:", dic[selecao]["vitorias"])
    print("Derrotas:", dic[selecao]["derrotas"])
    print("Gols marcados:", dic[selecao]["marcados"])
    print("Gols sofridos:", dic[selecao]["sofridos"])

print("-" * 50)
print("Pais campeao:", campeao)
print("-" * 50)