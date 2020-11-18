# Numero de açoes que vao ser cadastradas
n = int(input())

# Valores das açoes
valores = []
for i in range(n):
    aux = float(input())
    valores.append(aux)

# Dias que a pessoa pode viajar
k = int(input())

# Quantidade de dinheiro que sera levado na viagem
q = float(input())

dia_compra = 0
valor_compra = 0
dia_venda = 0
valor_venda = 0
qtde_acoes = 0
lucro = 0

# [quantidade_açoes, lucro, dia_compra, dia_venda, valor_compra, valor_venda]
maior_lucro = 0
info_maior_lucro = []

# Condição para caso o primeiro dia tenha o maior valor, o lucro vai ser 0 sempre que ele vender no mesmo dia,
# e negativo quando vender outro dia.
flag = True
continua = True
i = 0
while i < n and flag:

    if i == 0:
        valor_anterior = 0
        flag = False
        for m in range(n):
            if valores[m] > valor_anterior and m > 0:
                flag = True
            valor_anterior = valores[m]
        continua = False

    qtde_acoes = q // valores[i]
    resto = q - qtde_acoes * valores[i]

    j = 0
    while i + j < n and j < k + 1:
        if i + j < n:
            lucro = (qtde_acoes * valores[i + j]) - (q - resto)
            if lucro >= maior_lucro:
                maior_lucro = lucro
                info_maior_lucro = [qtde_acoes, lucro, i, j + i, valores[i], valores[j + i]]
            j += 1
    i += 1

print('Dia da compra:', info_maior_lucro[2] + 1)
print('Valor de compra: R$', format(info_maior_lucro[4], '.2f').replace('.', ','))
print('Dia da venda:', info_maior_lucro[3] + 1)
print('Valor de venda: R$', format(info_maior_lucro[5], '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', int(info_maior_lucro[0]))
print('Lucro: R$', format(info_maior_lucro[1], '.2f').replace('.', ','))