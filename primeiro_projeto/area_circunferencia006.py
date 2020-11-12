from math import pi, pow

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = pi * pow(float(raio), 2)
    print(f'A área do círculo é {area:.2f} cm')
