from string import Template

nome, idade = 'Ana', 30.9875
print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: %s Idade: %.2f' % (nome, idade))
print('Nome: %s Idade: %.2f %r %s' % (nome, idade, True, False))
print('Nome: %s Idade: %.2f %d %d' % (nome, idade, True, False))

print('Nome: {0} Idade: {1:.2f}'.format(nome, idade))

print(f'Nome: {nome} Idade: {idade:.2f}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))
