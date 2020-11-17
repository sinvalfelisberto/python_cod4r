# usando streamming
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
        # print('Nome: {}, Idade: {}'.format(registro.strip().split(',')))
# except IndexError:
#     pass
finally:
    print('Finnaly')
    arquivo.close()

if arquivo.closed:
    print('Arquivo foi fechado.')
