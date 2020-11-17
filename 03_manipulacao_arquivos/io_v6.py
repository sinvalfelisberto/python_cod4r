with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

        print('Arquivo atualizado', file=saida)

if arquivo.closed and saida.closed:
    print('Arquivos foram fechados')
