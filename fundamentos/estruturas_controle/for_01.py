for i in range(1, 11):
    print(f'i = {i}')

print('----------------------------')
for j in range(10):
    # for tradicional
    # pegando indice...
    # #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(f'j = {j}')

print('----------------------------')
for x in range(1, 11):
    print(f'******** Tabuada de {x} ********')
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
    print('\n')
