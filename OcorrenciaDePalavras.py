###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome:
# RA:
###################################################

# Leitura de dados
linhas = int(input())
frases = []
buscas = {
    "palavras": [],
    "ocorrencia": [],
    "similares": []
}
arrayPalavras = []

caractEspecial = ".?!,"

for i in range(0, linhas):
    frases.append(input().lower())
    for j in range(0, len(caractEspecial)):
        if caractEspecial[j] in frases[i]:
            frases[i] = frases[i].replace(caractEspecial[j], "")
    arrayPalavras.append(frases[i].split(" "))

palavras = int(input())

for i in range(0, palavras):
    buscas["palavras"].append(input().lower())
    buscas["ocorrencia"].append(0)
    buscas["similares"].append(0)

# Processamento do texto
for palavra in range(0, palavras):
    for texto in range(len(arrayPalavras)):
        for i in range(len(arrayPalavras[texto])):
            if buscas["palavras"][palavra] == arrayPalavras[texto][i]:
                buscas["ocorrencia"][palavra] += 1
            if buscas["palavras"][palavra] in arrayPalavras[texto][i] and buscas["palavras"][palavra] != arrayPalavras[texto][i]:
                buscas["similares"][palavra] += 1

# Saída de dados
for i in range(0, palavras):
    print("Palavra buscada:", buscas["palavras"][i])
    print("Ocorrencia:", buscas["ocorrencia"][i])
    print("Palavras similares:", buscas["similares"][i])

