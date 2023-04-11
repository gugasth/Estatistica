# Probabilidade de fechamento de cada relé
probabilidade_R1 = 0.3
probabilidade_R2 = 0.2
probabilidade_R3 = 0.1
probabilidade_R4 = 0.25

# Probabilidade de pelo menos um dos relés R1 e R2 fechar (série)
probabilidade_R1_R2 = probabilidade_R1 * probabilidade_R2

# Probabilidade de pelo menos um dos relés R3 e R4 fechar (série)
probabilidade_R3_R4 = probabilidade_R3 * probabilidade_R4

# Probabilidade de que pelo menos um dos pares em série tenha corrente entre L e M (paralelo)
probabilidade_com_corrente = 1 - (1 - probabilidade_R1_R2) * (1 - probabilidade_R3_R4)

# Imprimir o resultado
print("A probabilidade de haver corrente entre L e M é:", probabilidade_com_corrente)