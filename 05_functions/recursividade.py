def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


if __name__ == "__main__":
    valor = int(input('Digite um número para calcular o fatorial: '))
    resultado = fatorial(valor)
    print(f'{valor}! = {resultado}')

# coloca cada valor no stack
