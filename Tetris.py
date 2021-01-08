###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome:
# RA:
###################################################

"""
Esta função recebe seis parâmetros:
- tabuleiro: a configuração inicial do tabuleiro;
- altura_tabuleiro: o valor da altura do tabuleiro;
- largura_tabuleiro: o valor da largura do tabuleiro;
- peca: a configuração da peça a ser inserida;
- altura_peca: o valor da altura da peça a ser inserida;
- largura_peca: o valor da largura da peça a ser inserida.

A função deve retornar a configuração atualizada do tabuleiro
e o status do jogo ("O jogo deve continuar" ou "Fim de jogo")
"""


def verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro, peca, altura_peca, largura_peca):
    status_do_jogo = False

    return tabuleiro, status_do_jogo


# Leitura de dados

altura_tabuleiro, largura_tabuleiro = [int(x) for x in input().split()]

# Leitura do tabuleiro
tabuleiro = []
linha = input()
cont = 0

while altura_tabuleiro != cont:
    tabuleiro.append(linha)
    linha = input()
    cont = cont + 1

# Dica: use a função list() para transformar uma string numa lista de caracteres

altura_peca, largura_peca = [int(x) for x in input().split()]

# Leitura da peça
peca = []
cont = 0
tamPeca = input()

while altura_peca != cont:
    peca.append(tamPeca)
    tamPeca = input()
    cont = cont + 1

# Dica: use a função list() para transformar uma string numa lista de caracteres

# Impressão da configuração atualizada do tabuleiro


for linha in tabuleiro:
    print("".join(linha))

# Impressão do status do jogo
print(verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro, peca, altura_peca, largura_peca))
