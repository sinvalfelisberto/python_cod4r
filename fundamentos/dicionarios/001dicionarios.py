# Dicionário
pessoa = {'nome': 'Prof. Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
print(type(pessoa))
print(len(pessoa))
print(help(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('Tag'))
print(pessoa.get('Tag', []))
