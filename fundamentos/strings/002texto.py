valores_celulares = [850, 2230, 1500, 3500, 500, 700, 900, 1299]

# with open('valores_celulares.txt', 'w') as arquivo:
#     for valor in valores_celulares:
#         arquivo.write(str(valor) + '\n')

# with open('valores_celulares.txt', 'a') as arquivo:
#     for valor in valores_celulares:
#         arquivo.write(str(valor) + '\n')

# with open('valores_celulares.txt', 'r') as arquivo:
#     for valor in valores_celulares:
#         print(f'R$ {valor:.2f}')


with open('valores_celulares.txt', 'w') as arquivo:
    for valor in valores_celulares:
        arquivo.write("R$ " + (str(valor)) + '\n')

with open('valores_celulares.txt', 'r') as arquivo:
    for valor in valores_celulares:
        print(valor)
