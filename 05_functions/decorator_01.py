def log(function):
    def decorator(*args, ** kwargs):
        print(f'Inicio da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def subtracao(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))
    print(subtracao(3, y=2))
    print(soma(x=3, y=17))
    # print(soma(a=3, b=17)) gera erro: TypeError: soma() got an unexpected keyword argument 'a'
