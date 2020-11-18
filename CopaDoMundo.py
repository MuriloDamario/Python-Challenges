# Leitura da lista de seleções

selecoes = []
dic = {}
for i in range(16):
  selecao = input()
  selecoes.append(selecao)
  dic[selecao] = {"partidas": 0,
                  "vitorias": 0,
                  "derrotas": 0,
                  "penaltis": 0,
                  "normal": 0,
                  "marcados": 0,
                  "sofridos": 0}

# Leitura das partidas e processamento dos dados



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