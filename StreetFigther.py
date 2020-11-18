###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome:
# RA:
###################################################

# Leitura do hp dos lutadores
hp_Ryu = int(input())
hp_Ken = int(input())

hpRyu = hp_Ryu
hpKen = hp_Ken
# Leitura da sequência de golpes
hits_Ryu = 0
hits_Ken = 0
save_hits = []

while hp_Ken > 0 and hp_Ryu > 0:

    attack = int(input())
    save_hits.append(attack)

    if attack < 0:
        hits_Ken += 1
        hp_Ryu = hp_Ryu + attack
        attack = (-1) * attack
    else:
        hits_Ryu += 1
        hp_Ken = hp_Ken - attack

    if hp_Ken < 0:
        hp_Ken = 0

    if hp_Ryu < 0:
        hp_Ryu = 0

for i in range(len(save_hits)):

    if save_hits[i] < 0:
        hpRyu = hpRyu + save_hits[i]
        save_hits[i] = (-1) * save_hits[i]
        print("KEN APLICOU UM GOLPE: " + str(save_hits[i]))
    else:
        hpKen = hpKen - save_hits[i]
        print("RYU APLICOU UM GOLPE: " + str(save_hits[i]))

    if hpKen < 0:
        hpKen = 0

    if hpRyu < 0:
        hpRyu = 0

    print("HP RYU = " + str(hpRyu))
    print("HP KEN = " + str(hpKen))

# Impressão do vencedor e do número de golpes aplicados

if hp_Ken == 0:
    print("LUTADOR VENCENDOR: RYU")
else:
    print("LUTADOR VENCENDOR: KEN")

print("GOLPES RYU = " + str(hits_Ryu))
print("GOLPES KEN = " + str(hits_Ken))