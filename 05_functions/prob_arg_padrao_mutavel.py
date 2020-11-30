def fibonacci(sequencia=[0, 1]):
    # uso de mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))  # [0, 1, 1] 2516593103368
    print(fibonacci(inicio))  # [0, 1, 1, 2]
    restart = fibonacci()
    print(restart, id(restart))  # [0, 1, 1, 2, 3] 2516593103368
    assert restart == [0, 1, 1]
