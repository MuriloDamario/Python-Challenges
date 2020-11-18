# Leitura de dados
n1 = int(input(''))
n3 = int(input(''))
n4 = int(input(''))
n6 = int(input(''))

print(f'Primeiro: {n1}')
print(f'Terceiro: {n3}')
print(f'Quarto: {n4}')
print(f'Sexto: {n6}')

# Processamento e impressão da lista de possíveis apostas
print(f'Lista de apostas:')
for n2 in range(n1 + 1, n3):
    for n5 in range(n4 + 1, n6):
        if n1 % 2 != 0:
            if n2 % 2 == 0 and n5 % 2 != 0 and ((n1 + n2 + n3 + n4 + n5 + n6) % 7 != 0 and
                                                (n1 + n2 + n3 + n4 + n5 + n6) % 13 != 0):
                print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))
        else:
            if n2 % 2 != 0 and n5 % 2 == 0 and ((n1 + n2 + n3 + n4 + n5 + n6) % 7 != 0 and
                                                (n1 + n2 + n3 + n4 + n5 + n6) % 13 != 0):
                print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))