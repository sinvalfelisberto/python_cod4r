from math import pi, pow


def area_circulo(raio):
    return pi * pow(float(raio), 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = area_circulo(raio)
    print(f'Área do círculo: {area:.2f}')
