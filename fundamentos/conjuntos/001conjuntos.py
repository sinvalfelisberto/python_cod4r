# SET
conjunto = {1, 2, 3}
print(type(conjunto))
conjunto = set('codddd3r')
print('3' in conjunto, 4 not in conjunto)
print({3, 2, 1} == {1, 2, 3, 3})
print(conjunto)

# operações com conjuntos
cj1 = {1, 2}
cj2 = {3, 2}
print(cj1.union(cj2))
print(cj1.intersection(cj2))
print(cj1.update(cj2))
print(cj1)
print(cj2 <= cj1)
print(cj1 - {1})
