###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Nota de MC102
# Nome:
# RA:
###################################################

# Leitura de dados
N = int(input())
notas_lab = []
pesos_lab = []
nota_final = 0

for i in range(N):
    nota = float(input())
    notas_lab.append(nota)

for i in range(N):
    peso = float(input())
    pesos_lab.append(peso)

# Cálculo da média ponderada dos laboratórios
soma_lab = 0
divisor_lab = 0

for i in range(N):
    soma_lab = soma_lab + notas_lab[i] * pesos_lab[i]
    divisor_lab = divisor_lab + pesos_lab[i]

media = soma_lab / divisor_lab

# Verificação da situação do aluno
if media >= 5.0:
    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    # Caso o aluno tenha sido aprovado por nota
    print("Situacao: Aprovado por nota")
    nota_final = media
elif 2.5 <= media < 5.0:
    # Cálculo da nota do exame, caso o aluno tenha ido para o exame
    M = int(input())
    nota_exam = []
    pesos_exam = []
    soma_exam = 0
    divisor_exam = 0

    for i in range(M):
        lab = int(input())
        pesos_exam.append(pesos_lab[lab-1])

    for i in range(M):
        exam = float(input())
        soma_exam = soma_exam + exam * pesos_exam[i]
        divisor_exam = divisor_exam + pesos_exam[i]

    media_exam = soma_exam / divisor_exam
    nota_final = min(5, (media_exam + media) / 2)

    # Caso o aluno tenha sido aprovado no exame
    if nota_final == 5.0:
        print("Media laboratorios:", format(media, ".1f").replace(".", ","))
        print("Situacao: Aprovado no exame")
    else:
        print("Media laboratorios:", format(media, ".1f").replace(".", ","))
        # Caso o aluno tenha sido repravado no exame
        print("Situacao: Reprovado no exame")
elif media < 2.5:
    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    # Caso o aluno tenha sido reprovado por nota
    print("Situacao: Reprovado por nota")
    nota_final = media

# Saída de dados

print("Nota final:", format(nota_final, ".1f").replace(".", ","))
