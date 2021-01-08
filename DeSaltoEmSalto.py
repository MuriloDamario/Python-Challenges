"""
Dado um tabuleiro e duas posições (a,b) e (c,d), verifica se é
possível deslocar uma peça da posição (a,b) até a posição (c,d).

Em caso positivo, sua função deve retornar True e, em caso negativo,
False.
"""
def existe_caminho(tabuleiro, a, b, c, d):
#   ...


# Leitura de dados

n, m = [int(i) for i in input().split()]
tabuleiro = []
for _ in range(n):
	tabuleiro.append([int(i) for i in input().split()])
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]

# Verifica se existe caminho entre as posições dadas



# Impressão do resultado

print("({},{}) -> ({},{}):".format(a,b,c,d), caminho_1)
print("({},{}) -> ({},{}):".format(c,d,a,b), caminho_2)