#! python
# conding: utf-8

def get_dia_semana(dia):
    dias = {
        1: 'Domingo - Fim de Semana',
        2: 'Segunda - Semana',
        3: 'Terça - Semana',
        4: 'Quarta - Semana',
        5: 'Quinta - Semana',
        6: 'Sexta - Semana',
        7: 'Sábado - Fim de Semana',
    }
    return dias.get(dia, '_-* Inválido *-_')


if __name__ == '__main__':
    dia = int(input('Digite um numero(1-7): '))
    print(f'{dia}: {get_dia_semana(dia)}')
