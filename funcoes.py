import random

def rolar_dados(numero):
    lista = []
    for i in range(numero):
        x = random.randint(1, 6)
        lista.append(x)
    return lista