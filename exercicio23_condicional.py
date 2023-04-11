# Dados fornecidos
estudantes = {'Masculino': {'Biologia': 52, 'Exatas': 40, 'Humanas': 58},
              'Feminino': {'Biologia': 38, 'Exatas': 32, 'Humanas': 80}}

num_estudantes = 300;

# (a) Probabilidade de ser do sexo feminino e da área de humanas
prob_feminino_humanas = estudantes['Feminino']['Humanas'] / num_estudantes

# (b) Probabilidade de ser do sexo masculino e não ser da área de biológicas
prob_masculino_nao_biologia = (estudantes['Masculino']['Exatas'] + estudantes['Masculino']['Humanas']) / num_estudantes

# (c) Probabilidade de ser do sexo feminino dado que é da área de humanas
prob_feminino_dado_humanas = (estudantes['Feminino']['Humanas'] / num_estudantes) / ((estudantes['Feminino']['Humanas'] + estudantes['Masculino']['Humanas']) / num_estudantes)

# Resultados
print("Probabilidade de ser do sexo feminino e da área de humanas: ", prob_feminino_humanas)
print("Probabilidade de ser do sexo masculino e não ser da área de biológicas: ", prob_masculino_nao_biologia)
print("Probabilidade de ser do sexo feminino dado que é da área de humanas: ", prob_feminino_dado_humanas)