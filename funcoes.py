import random

def rolar_dados(numero):
    lista = []
    for i in range(numero):
        x = random.randint(1, 6)
        lista.append(x)
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, indice):
    dados_no_estoque.append(dados_rolados[indice])
    del dados_rolados[indice]
    lista = [dados_rolados, dados_no_estoque]
    return lista

def remover_dado(dados_rolados, dados_no_estoque, indice):
    dados_rolados.append(dados_no_estoque[indice])
    del dados_no_estoque[indice]
    lista = [dados_rolados, dados_no_estoque]
    return lista