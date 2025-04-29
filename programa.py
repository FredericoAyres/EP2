from funcoes import rolar_dados, guardar_dado, remover_dado, calcula_pontos_regra_simples, calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta, calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina, calcula_pontos_regra_avancada, faz_jogada, imprime_cartela

cartela = {'regra_simples': {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1}, 'regra_avancada': {'sem_combinacao': -1, 'quadra': -1, 'full_house': -1, 'sequencia_baixa': -1, 'sequencia_alta': -1, 'cinco_iguais': -1}}
imprime_cartela(cartela)

for i in range(12):

    dados_rolados = rolar_dados(5)
    dados_no_estoque = []
    num_rolagens = 0

    condicao = True
    while condicao == True:

        print('Dados rolados: {0}'.format(dados_rolados))
        print('Dados guardados: {0}'.format(dados_no_estoque))

        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        acao = input()
        while acao not in ['1', '2', '3', '4', '0']:
            print('Opção inválida. Tente novamente.')
            acao = input()
        else:
            if acao == '1':
                print('Digite o índice do dado a ser guardado (0 a 4):')
                indice = int(input())
                b = guardar_dado(dados_rolados, dados_no_estoque, indice)
                dados_rolados = b[0]
                dados_no_estoque = b[1]

            if acao == '2':
                print('Digite o índice do dado a ser removido (0 a 4):')
                indice = int(input())
                c = remover_dado(dados_rolados, dados_no_estoque, indice)
                dados_rolados = c[0]
                dados_no_estoque = c[1]

            if acao == '3':
                if num_rolagens < 2:
                    x = rolar_dados(len(dados_rolados))
                    dados_rolados = x
                    num_rolagens += 1
                else:
                    print('Você já usou todas as rerrolagens.')

            if acao == '4': 
                imprime_cartela(cartela)

            if acao == '0':
                lista_dados = dados_rolados + dados_no_estoque
                print('Digite a combinação desejada:')
                combinacao = input()
                while condicao == True:
                    while combinacao not in ['1', '2', '3', '4', '5', '6'] and combinacao not in cartela['regra_avancada']:
                        print('Combinação inválida. Tente novamente.')
                        combinacao = input()
                    while (combinacao in ['1', '2', '3', '4', '5', '6'] or combinacao in cartela['regra_avancada']) and condicao == True:
                        if combinacao in ['1', '2', '3', '4', '5', '6']:
                            x = int(combinacao)
                            if cartela['regra_simples'][x] != -1:
                                    print('Essa combinação já foi utilizada.')
                                    combinacao = input()
                                    if combinacao in ['1', '2', '3', '4', '5', '6']:
                                        x = int(combinacao)
                            else:
                                cartela = faz_jogada(lista_dados, combinacao, cartela)
                                condicao = False
                        elif combinacao in cartela['regra_avancada']:
                            if cartela['regra_avancada'][combinacao] != -1:
                                print('Essa combinação já foi utilizada.')
                                combinacao = input()
                            else:
                                cartela = faz_jogada(lista_dados, combinacao, cartela)
                                condicao = False

pontuacao = 0
for x in cartela['regra_simples']:
    pontuacao += cartela['regra_simples'][x]
if pontuacao >= 63:
    pontuacao += 35
for x in cartela['regra_avancada']:
    pontuacao += cartela['regra_avancada'][x]

imprime_cartela(cartela)
print('Pontuação total: {0}'.format(pontuacao))