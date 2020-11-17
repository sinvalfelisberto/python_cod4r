# retorna o termo solicitado
import sys
import errno


def help():
    print('Digite um valor válido')
    print(f'Sintaxe: python {sys.argv[0][2:]} <valor>')


def fibonacci(termos):
    resultado = [0, 1]
    for i in range(2, termos):
        i
        resultado.append(sum(resultado[-2:]))
    return resultado[-1]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print('Digite um valor numérico.')
        sys.exit(errno.EINVAL)
    elif int(sys.argv[1]) > 200:
        print('Valor muito alto! Seu computador vai travar!')
        sys.exit(errno.EPERM)
    else:
        termo = int(sys.argv[1])
        print(f'O termo desejado é {fibonacci(termo)}')
