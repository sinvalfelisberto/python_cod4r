# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# retorna o termo solicitado
def fibonacci(termos):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == termos:
            break
    return resultado[-1]


if __name__ == '__main__':
    termo = int(input('Digite o termo desejado: '))
    print(f'O termo desejado é {fibonacci(termo)}')
