import random

# função que verifica se um operador alcançou sua cota de produção
def alcancou_cota(curso):
    if curso:
        return random.random() < 0.9
    else:
        return random.random() < 0.65

# função que simula se um operador passou pelo curso
def passou_pelo_curso():
    return random.random() < 0.5

# número de iterações
num_iteracoes = 10000

# contador de operadores que passaram pelo curso e alcançaram a cota de produção
contador_passou_pelo_curso_e_alcancou_cota = 0

# contador de operadores que alcançaram a cota de produção
contador_alcancou_cota = 0

# simulação
for i in range(num_iteracoes):
    passou_curso = passou_pelo_curso()
    alcancou_cota_producao = alcancou_cota(passou_curso)
    if passou_curso:
        contador_passou_pelo_curso_e_alcancou_cota += alcancou_cota_producao
    contador_alcancou_cota += alcancou_cota_producao

# cálculo da probabilidade
probabilidade = contador_passou_pelo_curso_e_alcancou_cota / contador_alcancou_cota

# resultado
print("a probabilidade de ter passado pelo curso, visto que alcançou a cota de produção é: {:.4f}".format(probabilidade))