from math import pi, pow
import sys


def area_circulo(raio):
    return pi * pow(float(raio), 2)


if __name__ == '__main__':
    raio = sys.argv[1]
    area = area_circulo(raio)
    print(f'Área do círculo: {area:.2f}')

"""na hora de executar no terminal, devemos adicionar
o argumento no final da linha de comando
exemplo
python .\area_circulo_010.py 3
esse 3 é o raio, que é o argumento."""
