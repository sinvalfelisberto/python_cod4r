from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)
while numero_informado != numero_secreto:
    numero_informado = int(input('Digite um número entre 0 e 9: '))

print(f'Número secreto {numero_secreto} foi encontrado! Parabéns!')
