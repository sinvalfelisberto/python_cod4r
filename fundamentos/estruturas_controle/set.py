PALAVRAS_PROIBIDAS = {'política', 'futebol', 'religião', }

textos = [
    'João gosta de política e futebol',
    'Odeio quem fala mal de religião',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas', intersecao)
    else:
        print('Texto autorizado', texto)
