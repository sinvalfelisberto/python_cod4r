def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(10, 15))
    print(soma_3(10, 15, 20))
    # packing = empacotando os parâmetros em uma tupla
    print(soma_n(1))
    print(soma_n(10, 20))
    print(soma_n(10, 20, 30, 50, 100, 350, 345, 95))
    # unpacking = pegar os parâmetros de um lista/tupla...
    nums = [3, 4, 13]
    nums1 = (7, 3, 90)
    print(soma_n(*nums))
    print(soma_n(*nums1))
