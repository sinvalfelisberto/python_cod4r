from math import pi, pow
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def area_circulo(raio):
    return pi * pow(float(raio), 2)


def help():
    print(TerminalColor.ERRO, "É necessário informar o raio do círculo")
    print(f' Sintaxe: python {sys.argv[0]} <raio>', TerminalColor.NORMAL)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO, 'O raio deve ser um valor numérico.',
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = area_circulo(raio)
    print(f'Área do círculo: {area:.2f}')
