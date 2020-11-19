def tag_bloco(texto, classe='sucess'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # testes de assertions
    assert tag_bloco('Incluido com sucesso') == \
        '<div class="sucess">Incluido com sucesso</div>'
    assert tag_bloco('Impossivel excluir', 'error') == \
        '<div class="error">Impossivel excluir</div>'
    print(tag_bloco('bloco'))
