def preencher_tabela():
    matriz = [
        ('Fabricante / Ano', '2013', '2014', '2015', '2016', '2017', '2018'),
        ('Fiat',),
        ('Ford',),
        ('GM',),
        ('Wolkswagen',)
    ]

    for lin in range(1, 5):  # índices para acessa linhas
        for v in range(1, 7):  # índices para acessa colunas
            matriz[lin] += int(input().strip()),

    return matriz


def analise_venda_ano(tabela):
    # Ano para nálise
    ano = input().strip()
    # índice do ano
    indice_ano = tabela[0].index(ano)

    # Quem mais vendeu?
    valores = []
    for linha in range(1, 5):  # índices para acessa linhas
        valores.append(tabela[linha][indice_ano])

    # MAior valor vendido no Ano
    maior_venda = max(valores)
    # Emoresa
    indice_empr = valores.index(maior_venda) + 1
    empresa = tabela[indice_empr][0]

    return empresa, maior_venda, ano


def analise_venda_periodo(tabela):
    # Quem mais vendeu em todo periodo?
    maior_venda = 0
    # marca = None
    ano = None
    for colun in range(1, 7):  # índices para acessa linhas
        valor_na_tabela = 0
        for linha in range(1, 5):  # índices para acessa colunas
            valor_na_tabela += tabela[linha][colun]

        if valor_na_tabela > maior_venda:
            ano = tabela[0][colun]  # Ano
            maior_venda = valor_na_tabela
            valor_na_tabela = 0
        else:
            valor_na_tabela = 0

    return ano, maior_venda


def analise_fabricantes(tabela):
    empresas = []
    valores = []

    for linha in range(1, 5):

        # Resultado de cada empresa no período
        for ano in range(1, 7):  # índices para acessa linhas
            valores.append(tabela[linha][ano])

        media = sum(valores) / len(valores)
        empresas.append((tabela[linha][0], round(media, 2)))
        valores = []

    return empresas


def main():
    tabela = preencher_tabela()

    # A fabricante que mais vendeu em... e valor
    empresa_ano, melhor_venda_ano, ano = analise_venda_ano(tabela)
    print(f"A fabricante que mais vendeu em {ano} foi a {empresa_ano} com {melhor_venda_ano} mil unidades.")
    # A média anual de vendas de cada fabricante entre 2013 e 2018 foi:
    melhor_ano, maior_volume = analise_venda_periodo(tabela)
    print(f"O ano de maior volume geral de vendas foi {melhor_ano} com {maior_volume} mil unidades.")
    # A média anual de vendas de cada fabricante entre 2013 e 2018 foi:
    resultado = analise_fabricantes(tabela)
    print('A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')
    for empresa, media_anual in resultado:
        print(f"A {empresa} vendeu em média {media_anual} unidades por ano.")


if __name__ == '__main__':
    main()