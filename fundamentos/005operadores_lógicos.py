print(True or False)
print(7 != 3 and 2 > 3)
# XOR - ou exclusisvo
# print(True != False)
# print(False != True)
# print(True != True)
# print(False != False)

# Operadores bit-a-bit
'''
&, | e ^
operam no valor binário de um
dado.
'''

# exemplo
saldo = 1000
salario = 4000
despesas = 2700

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
# if meta == True:
#     print("Meta batida")
# else:
#     print("Meta não batida")
