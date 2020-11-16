# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(termos):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == termos:
            break
    return resultado


if __name__ == '__main__':
    quantidade = int(input('Qtd de termos: '))
    for fib in fibonacci(quantidade):
        print(fib, end=', ')
