import sys
import errno


def conceito(valor):
    nota = float(valor)
    if nota > 10:
        return 'Nota inválida'
    elif nota > 9:
        return 'A'
    elif nota > 8:
        return 'A-'
    elif nota > 7:
        return 'B'
    elif nota > 6:
        return 'B-'
    elif nota > 5:
        return 'C'
    elif nota > 4:
        return 'C-'
    elif nota > 3:
        return 'D'
    elif nota > 2:
        return 'D-'
    elif nota > 1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        'Nota inválida.'


def help():
    print('É necessário informar a nota do aluno!')
    print(f'Sintaxe: {sys.argv[0][2:]} <nota>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print('A nota deve ser um valor numérico.')
        print('tipo: sys.argv[1] =', type(sys.argv[1]))
        sys.exit(errno.EINVAL)
    nota = float(sys.argv[1])
    print('Conceito do Aluno:', conceito(nota))
    print(type(sys.argv[1]))
