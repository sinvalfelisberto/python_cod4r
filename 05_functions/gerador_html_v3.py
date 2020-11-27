def tag_bloco(conteudo, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)  # generator
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(inline=False, conteudo='Bom demais'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
