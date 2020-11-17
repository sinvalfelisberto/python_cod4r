def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade.'
    elif idade in range(18, 65):
        return 'Adulto.'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida.'


if __name__ == '__main__':
    # idades = (17, 35, 87, 119, -2)
    # for idade in idades:
    for idade in (17, 35, 87, 119, -2):
        print(f'{idade} anos: {faixa_etaria(idade)}')
