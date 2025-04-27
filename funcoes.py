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

def calcula_pontos_regra_simples(lista):
    dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in lista:
        soma = 0
        for j in lista:
            if j == i:
                soma += j
        dicionario[i] = soma
    return dicionario

def calcula_pontos_soma(lista):
    soma = 0
    for x in lista:
        soma += x
    return soma

def calcula_pontos_sequencia_baixa(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
        return 15
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 15
    if 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 15
    else:
        return 0 
    
def calcula_pontos_sequencia_alta(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 30
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 30
    else:
        return 0
    
def calcula_pontos_full_house(lista):
    qnt = [0, 0, 0, 0, 0, 0]
    soma = 0
    for x in lista:
        qnt[x-1] += 1
        soma += x
    if 3 in qnt and 2 in qnt:
        return soma
    else:
        return 0

def calcula_pontos_quadra(lista):
    qnt = [0, 0, 0, 0, 0, 0]
    soma = 0
    for x in lista:
        qnt[x-1] += 1
        soma += x
    qnt_max = 0
    for y in qnt:
        if y > qnt_max:
            qnt_max = y
    if qnt_max >= 4:
        return soma
    else:
        return 0

def calcula_pontos_quina(lista):
    qnt = [0, 0, 0, 0, 0, 0]
    for x in lista:
        qnt[x-1] += 1
    qnt_max = 0
    for y in qnt:
        if y > qnt_max:
            qnt_max = y
    if qnt_max >= 5:
        return 50
    else:
        return 0

def calcula_pontos_regra_avancada(lista):
    dicionario = {'cinco_iguais': 0, 'full_house': 0, 'quadra': 0, 'sem_combinacao': 0, 'sequencia_alta': 0, 'sequencia_baixa': 0}
    a = calcula_pontos_quina(lista)
    if a != 0:
        dicionario['cinco_iguais'] = a
    b = calcula_pontos_full_house(lista)
    if b != 0:
        dicionario['full_house'] = b
    c = calcula_pontos_quadra(lista)
    if c != 0:
        dicionario['quadra'] = c
    d = calcula_pontos_soma(lista)
    if d != 0:
        dicionario['sem_combinacao'] = d
    e = calcula_pontos_sequencia_alta(lista)
    if e != 0:
        dicionario['sequencia_alta'] = e
    f = calcula_pontos_sequencia_baixa(lista)
    if f != 0:
        dicionario['sequencia_baixa'] = f
    return dicionario