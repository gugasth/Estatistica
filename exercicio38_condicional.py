import random

# probabilidades de escolher cada urna
prob_urna_1 = 1/3
prob_urna_2 = 1/2
prob_urna_3 = 1/6

# probabilidades de retirar uma bola branca de cada urna
prob_branca_urna_1 = 3/8
prob_branca_urna_2 = 4/6
prob_branca_urna_3 = 1/4

# variáveis para contar a quantidade de bolas brancas e total de bolas retiradas
total_bolas_brancas = 0
total_bolas_retiradas = 0

# realiza a retirada das bolas 10.000 vezes
for i in range(10000):
    # escolhe uma urna de acordo com as probabilidades
    urna_escolhida = random.choices([1, 2, 3], [prob_urna_1, prob_urna_2, prob_urna_3])[0]

    # retira uma bola da urna escolhida
    if urna_escolhida == 1:
        bola_branca = random.choices([True, False], [prob_branca_urna_1, 1 - prob_branca_urna_1])[0]
    elif urna_escolhida == 2:
        bola_branca = random.choices([True, False], [prob_branca_urna_2, 1 - prob_branca_urna_2])[0]
    else:
        bola_branca = random.choices([True, False], [prob_branca_urna_3, 1 - prob_branca_urna_3])[0]

    # atualiza as contagens de bolas brancas e total de bolas retiradas
    total_bolas_brancas += bola_branca
    total_bolas_retiradas += 1

# calcula a probabilidade de retirar uma bola branca
prob_branca = total_bolas_brancas / total_bolas_retiradas

# imprime o resultado
print("a probabilidade de retirar uma bola branca é: ", prob_branca)
