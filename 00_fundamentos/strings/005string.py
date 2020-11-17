# Magic Methods

a = '123'
b = ' de oliveira 4'

print(a + b)  # operação de alto nível
print(a.__add__(b))
print(str.__add__(a, b))

print(len(a))
print(a.__len__())
print('1' in a)
print(a.__contains__('1'))
