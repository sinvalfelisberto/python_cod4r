from math import pi, pow
import sys


def area_circulo(raio):
    return pi * pow(float(raio), 2)


def help():
    print("é necessário informar o raio do círculo")
    print(f'Sintaxe: python {sys.argv[0]} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = area_circulo(raio)
        print(f'Área do círculo: {area:.2f}')
