# probabilidade de um suspeito ser inocente, considerando que apenas 5% dos suspeitos já cometeram um crime
p_A = 0.95

# probabilidade de o soro indicar que o suspeito é culpado, dado que ele é inocente
p_B_dado_que_A_ocorreu = 0.01 

# probabilidade de o soro indicar que o suspeito é culpado, dado que ele é culpado
p_B_dado_que_A_nao_ocorreu = 0.90

# probabilidade de um suspeito ser culpado
p_not_A = 0.05

# teorema de bayes
p_A_given_B = (p_A * p_B_dado_que_A_ocorreu) / ((p_A * p_B_dado_que_A_ocorreu) + (p_not_A * p_B_dado_que_A_nao_ocorreu))

# imprimindo o resultado
print("Probabilidade de ser inocente, dado que o soro indicou culpado:", p_A_given_B)