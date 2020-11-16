#! python
# conding: utf-8

def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return dias.get(dia, '_-* Inválido *-_')


def get_tipo_dia(dia):
    if dia in range(2, 7):
        return 'Dia de semana!'
    if dia == 1 or dia == 7:
        return 'Final de Semana!'
    else:
        return ''


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)} - {get_tipo_dia(dia)}')
