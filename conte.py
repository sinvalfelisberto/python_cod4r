import time


def calcule(valor):
    for i in range(valor):
        print(valor - 1)
        time.sleep(0.9)


calcule(30)
