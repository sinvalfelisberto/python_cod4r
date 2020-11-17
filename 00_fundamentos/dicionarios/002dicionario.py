pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa.pop('idade')
pessoa.update({'idade': 40, 'Sexo': 'M'})
del pessoa['cursos']
pessoa.clear()
print(pessoa)
