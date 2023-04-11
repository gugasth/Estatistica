import random

def comprar_chiclete():
    return random.choice(["vermelho", "verde", "amarelo"])

def comprar_ate_amarela():
    sequencia = []
    while True:
        bola = comprar_chiclete()
        sequencia.append(bola)
        if bola == "amarelo":
            break
    return sequencia

sequencia = comprar_ate_amarela()
print("o espaço amostral é infinito")
print("sequência de cores até obter uma bola amarela:")
print(sequencia)
