# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')
from random import randint


def sortear_dado():
    return randint(1, 6)


for face in range(1, 7):
    if face % 2 == 1:
        continue
    elif face == sortear_dado():
        print(f'Acertou! --> face = {face}')
        break
else:
    print('Não acertou o número!')
