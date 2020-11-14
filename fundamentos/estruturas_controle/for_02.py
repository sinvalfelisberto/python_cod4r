palavra = 'paralelepipedo'

# string
for letra in palavra:
    print(letra, end='_')

print('\n')
for posicao, letra in enumerate(palavra):
    print(posicao+1, 'a letra: ', letra)

# lista
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

# tupla
dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for posicao, dia in enumerate(dias_semana):
    print(f'{posicao+1}o dia: ', dia)

# set
for letra in set('muito legal'):
    print(letra)

# conjuto
for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
