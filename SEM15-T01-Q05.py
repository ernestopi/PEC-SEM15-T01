def preencher_tabela():
    array = [
        [
            ('2014'),
            ('Meses', 1, 2, 3, 'Total'),
            [('Janeiro'), []],
            [('Fevereiro'), []],
            [('Março'), []],
            [('Abril'), []],
            [('Maio'), []],
            [('Junho'), []],
            [('Julho'), []],
            [('Agosto'), []],
            [('Setembro'), []],
            [('Outubro'), []],
            [('Novembro'), []],
            [('Dezembro'), []]
        ],
        [
            ('2015'),
            ('Meses', 1, 2, 3, 'Total'),
            [('Janeiro'), []],
            [('Fevereiro'), []],
            [('Março'), []],
            [('Abril'), []],
            [('Maio'), []],
            [('Junho'), []],
            [('Julho'), []],
            [('Agosto'), []],
            [('Setembro'), []],
            [('Outubro'), []],
            [('Novembro'), []],
            [('Dezembro'), []]
        ],
        [
            ('2016'),
            ('Meses', 1, 2, 3, 'Total'),
            [('Janeiro'), []],
            [('Fevereiro'), []],
            [('Março'), []],
            [('Abril'), []],
            [('Maio'), []],
            [('Junho'), []],
            [('Julho'), []],
            [('Agosto'), []],
            [('Setembro'), []],
            [('Outubro'), []],
            [('Novembro'), []],
            [('Dezembro'), []]
        ],
        [
            ('2017'),
            ('Meses', 1, 2, 3, 'Total'),
            [('Janeiro'), []],
            [('Fevereiro'), []],
            [('Março'), []],
            [('Abril'), []],
            [('Maio'), []],
            [('Junho'), []],
            [('Julho'), []],
            [('Agosto'), []],
            [('Setembro'), []],
            [('Outubro'), []],
            [('Novembro'), []],
            [('Dezembro'), []]
        ]
    ]

    for tabela in range(4):  # Índices para acessa tabela
        for colun in range(1, 4):  # inserir colunas
            for lin in range(2, 14):  # Indice linhas
                array[tabela][lin][1].append(int(input().strip()))  # Concatena valores na lista

    return array


def dados_filiais_anual(array):
    valores = []

    for tabela in range(4):  # Índices para acessa tabela
        ano = (array[tabela][0])  # Ano
        for colun in range(3):
            for linha in range(2, 14):  # Indice para cada linha 12 meses

                # Ano fixo

                # filial fixa
                filial = array[tabela][1][colun + 1]
                # mes muda
                mes = array[tabela][linha][0]  # Coluna fixa [0]

                # Valor muda para cada mês
                valor = array[tabela][linha][1][colun]  # Coluna_valor fixa
                # print(valor)
                # inserir (ano, filial, mes, valor)
                valores.append((ano, filial, mes, valor))

    # Deve retornar uma lista com tuplas:
    # (ano, filial, mes, valor)
    return valores


def main():
    tabela = preencher_tabela()
    dados = dados_filiais_anual(tabela)

    # Valores para soma e análise anual
    contador_ano = 1
    contador_ano_2 = 1
    valores_cada_filial_ano = []
    valores_total_filiais_ano = []
    valor_total_periodo = []
    for ano, filial, mes, valor in dados:
        print(f'{ano};Filial {filial};{mes};{valor}')
        valores_cada_filial_ano.append(valor)
        valores_total_filiais_ano.append(valor)

        if contador_ano == 12:  # Mude para 11 equivale 1 ano
            # Ano
            # Somar valores filial
            soma_filial = sum(valores_cada_filial_ano)
            print(f'TOTAL {ano} FILIAL {filial};{soma_filial}')
            # Zerando
            contador_ano = 0
            valores_cada_filial_ano = []

        if contador_ano_2 == 36:  # Mude para qtd de meses * qtd filiais
            soma_filiais_total = sum(valores_total_filiais_ano)
            print(f'TOTAL {ano} TODAS FILIAIS;{soma_filiais_total}')

            contador_ano_2 = 0

            valor_total_periodo.append(soma_filiais_total)
            valores_total_filiais_ano = []

        contador_ano += 1
        contador_ano_2 += 1
    # Resultado total de todo período
    total_periodo = sum(valor_total_periodo)
    print(f'TOTAL PERÍODO TODAS FILIAIS;{total_periodo}')


if __name__ == '__main__':
    main()