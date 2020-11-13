from math import pi, pow
import sys
import errno


def area_circulo(raio):
    return pi * pow(float(raio), 2)


def help():
    print("é necessário informar o raio do círculo")
    print(f'Sintaxe: python {sys.argv[0]} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor numérico.')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = area_circulo(raio)
    print(f'Área do círculo: {area:.2f}')
