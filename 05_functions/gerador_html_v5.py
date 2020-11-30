bloco_atrs = ('bloco_acesskey', 'bloco_id')
ul_atrs = ('ul_style', 'ul_id')


def filtrar_atrs(informados, suportados):
    return ' '.join(f'{k.split("_") [-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='sucess', inline=False, **novos_atrs):
    # *ARGS gera uma tupla com os argumentos necessários para a função
    tag = 'span' if inline else 'div'
    # *ARGS gera uma tupla com os argumentos necessários para a função
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


# *ARGS gera uma tupla com os argumentos necessários para a função
def tag_lista(*itens, **novos_atrs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {filtrar_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    # print(tag_bloco('bloco'))
    # print(tag_bloco('inline e classe', classe='info', inline=True))
    # print(tag_bloco('inline', inline=True))
    # print(tag_bloco('falhou', classe='error'))
    # print(tag_bloco(inline=False, conteudo='Bom demais'))
    # print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    # print(tag_bloco(tag_lista,
    #                 'Sábado', 'Domingo', classe='error', inline=False))
    # # Aqui, depois de chamar a função, são listados os valores que irão compor
    # # a tupla que será usada pelo *args
    # print(tag_bloco(tag_lista,
    #                 'Sábado', 'Domingo', classe='info', inline=True))
    print(tag_bloco(tag_lista, 'item 1', 'item 2', classe='Info',
                    bloco_acesskey='m', bloco_id='conteudo', ul_id='lista',
                    ul_style='color:red'))
