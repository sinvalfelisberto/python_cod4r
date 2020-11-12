#! python
from math import pi, pow
import sys


def area_circulo(raio):
    return pi * pow(float(raio), 2)


if __name__ == '__main__':
    print(f'\n{sys.argv[0]}')
    raio = input('Informe o raio: ')
    area = area_circulo(raio)
    print(f'Área do círculo: {area:.2f}')
