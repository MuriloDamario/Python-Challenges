# Leitura de dados
num_produtos = int(input())

cabecalho = input().split(",")

info_produtos = []
for n in range(num_produtos):
    info_produtos.append(input().split(","))

for i in range(len(info_produtos)):
    info_produtos[i][1] = int(info_produtos[i][1])
    info_produtos[i][2] = int(info_produtos[i][2])
    info_produtos[i][3] = int(info_produtos[i][3])

aux = [input().split(" ")]
ordem = []
for n in range(len(aux[0])):
    ordem.append(aux[0][n])
ordem.reverse()


# Ordenação dos dados
def insertion_sort(matriz, col):
    for i in range(1, len(matriz)):
        key = matriz[i]
        j = i - 1
        while j >= 0 and key[col] < matriz[j][col]:
            matriz[j + 1] = matriz[j]
            j -= 1
        matriz[j + 1] = key


for j in range(len(ordem)):
    if ordem[j] == "Produto":
        insertion_sort(info_produtos, 0)
    # info_produtos.sort(key=lambda x: x[0])
    elif ordem[j] == "Setembro":
        insertion_sort(info_produtos, 1)
        # info_produtos.sort(key=lambda x: x[1])
    elif ordem[j] == "Outubro":
        insertion_sort(info_produtos, 2)
        # info_produtos.sort(key=lambda x: x[2])
    elif ordem[j] == "Novembro":
        insertion_sort(info_produtos, 3)
        # info_produtos.sort(key=lambda x: x[3])

# Saída dos dados
info_produtos.insert(0, cabecalho)
for linha in info_produtos:
    print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in linha[1:]))
