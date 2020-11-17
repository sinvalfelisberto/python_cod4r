from math import pi, pow


def area_circulo(raio):
    print('Área do círculo:', (pi * pow(float(raio), 2)))


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area_circulo(raio)
