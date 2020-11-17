import csv

with open('pessoas.csv') as entrada:
    with open('pessoas_02.txt', 'w') as saida:
        for pessoa in csv.reader(entrada):
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
    print('Novo arquivo atualizado')

if entrada.closed and saida.closed:
    print('Arquivos fechados.')
