###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Filtros de Imagens
# Nome:
# RA:
###################################################


"""
Função que recebe uma imagem e imprime essa imagem no formato PGM
"""
import copy


def imprime_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(x) for x in imagem[i]))


'''
Função que retorna a mediana de uma lista. Se o tamanho da lista
for par, a função retorna a parte inteira da média entre os elementos
centrais
'''


def mediana(lista):
    lista_ordenada = sorted(lista)
    elemento_central = len(lista_ordenada) // 2
    if len(lista) % 2 == 1:
        return lista_ordenada[elemento_central]
    else:
        # retorna a parte inteira da média entre os elementos centrais
        return (lista_ordenada[elemento_central - 1] + lista_ordenada[elemento_central]) // 2


''' 
Função que recebe a matriz que representa a imagem original e
retorna a imagem resultante da aplicação do filtro negativo 
'''


def filtro_negativo(imagem):
    for row in range(len(imagem)):
        for col in range(len(imagem[0])):
            imagem[row][col] = 255 - imagem[row][col]
    return imagem


'''
Função que recebe a matriz que representa a imagem original e 
retorna a imagem resultante da aplicação do filtro da mediana
'''


def filtro_mediana(imagem):
    img = copy.deepcopy(imagem)

    for row in range(len(img)):
        for col in range(len(img[0])):
            arr = []
            if row == 0 and col == 0:
                for i in range(0, 2):
                    for j in range(0, 2):
                        arr.append(img[i][j])
                imagem[row][col] = mediana(arr)
            elif row == len(img) - 1 and col == 0:
                for i in range(-2, 0):
                    for j in range(0, 2):
                        arr.append(img[len(img) + i][j])
                imagem[row][col] = mediana(arr)
            elif row == 0 and col == len(img[0]) - 1:
                for i in range(0, 2):
                    for j in range(-2, 0):
                        arr.append(img[i][len(img[0]) + j])
                imagem[row][col] = mediana(arr)
            elif row == len(img) - 1 and col == len(img[0]) - 1:
                for i in range(-2, 0):
                    for j in range(-2, 0):
                        arr.append(img[len(img) + i][len(img[0]) + j])
                imagem[row][col] = mediana(arr)
            elif row == 0 and col != 0:
                for i in range(0, 2):
                    for j in range(-1, 2):
                        arr.append(img[i][col + j])
                imagem[row][col] = mediana(arr)
            elif row == len(img) - 1 and col != 0:
                for i in range(-2, 0):
                    for j in range(-1, 2):
                        arr.append(img[len(img) + i][col + j])
                imagem[row][col] = mediana(arr)
            elif row != 0 and col == 0:
                for i in range(-1, 2):
                    for j in range(0, 2):
                        arr.append(img[row + i][j])
                imagem[row][col] = mediana(arr)
            elif row != 0 and col == len(img[0]) - 1:
                for i in range(-1, 2):
                    for j in range(-2, 0):
                        arr.append(img[row + i][len(img[0]) + j])
                imagem[row][col] = mediana(arr)
            else:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        arr.append(img[row + i][col + j])
                imagem[row][col] = mediana(arr)
    return imagem


'''
Função que recebe três parâmetros: 

imagem: matriz que representa a imagem original
M: matriz núcleo
D: divisor

Essa função retorna a imagem resultante da aplicação de um filtro 
que usa convolução
'''


def convolucao(imagem, M, D):
    img = copy.deepcopy(imagem)
    p = 0
    img_result = []
    for row in range(1, len(img) - 1):
        img_result.append([])
        for col in range(1, len(img[0]) - 1):
            l1 = M[0][0] * img[row - 1][col - 1] + M[0][1] * img[row - 1][col] + M[0][2] * img[row-1][col+1]
            l2 = M[1][0] * img[row][col-1] + M[1][1] * img[row][col] + M[1][2] * img[row][col+1]
            l3 = M[2][0] * img[row+1][col-1] + M[2][1] * img[row+1][col] + M[2][2] * img[row+1][col+1]
            p = (l1 + l2 + l3) // D
            if p < 0:
                p = 0
            elif p > 255:
                p = 255
            img_result[row - 1].append(p)

    return img_result


# Leitura da entrada

filtro = input()
_ = input()  # P2 (linha a ser ignorada)

m, n = [int(x) for x in input().split()]

_ = input()  # 255 - linha a ser ignorada

imagem = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem.append(linha)

# Aplica o filtro
if filtro == "negativo":
    filtro_negativo(imagem)
elif filtro == "mediana":
    filtro_mediana(imagem)
elif filtro == "blur":
    M = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    imagem = convolucao(imagem, M, 1)
elif filtro == "sharpen":
    M = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    imagem = convolucao(imagem, M, 9)
elif filtro == "edge-detect":
    M = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    imagem = convolucao(imagem, M, 1)
# Imprime a imagem gerada
imprime_imagem(imagem)
