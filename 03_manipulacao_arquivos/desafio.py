
import csv

if __name__ == '__main__':
    try:
        with open('desafio-ibge.csv') as arquivo:
            dados = arquivo.read().decode('latin1')
            with open('desafio_ibge.txt', 'w') as saida:
                for campo in csv.reader(dados.splitlines()):
                    print('{}: {}'.format(campo[8], campo[3]), file=saida)
                print('Arquivo gravado com sucesso.', file=saida)
                print('Arquivo gravado com sucesso.')
    finally:
        print('Finnaly')
    if arquivo.closed and saida.closed:
        print('Arquivos fechados')
