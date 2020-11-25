# *ARGS gera uma tupla com os argumentos necessários para a função
def tag_bloco(conteudo, *args, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    # *ARGS gera uma tupla com os argumentos necessários para a função
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


# *ARGS gera uma tupla com os argumentos necessários para a função
def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(inline=False, conteudo='Bom demais'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista,
                    'Sábado', 'Domingo', classe='error', inline=False))
    # Aqui, depois de chamar a função, são listados os valores que irão compor
    # a tupla que será usada pelo *args
    print(tag_bloco(tag_lista,
                    'Sábado', 'Domingo', classe='error', inline=True))
