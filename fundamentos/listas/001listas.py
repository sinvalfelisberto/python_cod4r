lista = []  # lista é dinâmica e os itens são heterogênios.
print(type(lista))
# print(dir(lista))
# print(help(lista))
print(len(lista))
lista.append(1)
lista.append(5)
print(len(lista))
print(lista)
nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)
print(nova_lista.remove('Ana'))
print(nova_lista)
nova_lista.reverse()  # lista é um elemento mutável, diferente da string(array)
print(nova_lista)
# cuidados com o uso de lista heterogênias.
print('fim')
