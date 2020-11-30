strong


def tag(tag, *args, **kwargs):
    pass


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', 'e'),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )


# resultado:
# <p class="alert"><span>Curso Python 3, por</span><strong id="jf">Juracy Filho</strong><span> e </span><strong id="ll">Leonardo Leitão</strong><span>.</span>
