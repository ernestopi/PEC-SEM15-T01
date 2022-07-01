
def faz_matriz_quadrada(dimensao):
    matriz = []
    for lin in range(dimensao):  # Linhas
        linha = []  # Cada linha é uma lista (vetor)
        for col in range(dimensao):  # Colunas
            # Gera número aleatório entre 1 e 50
            linha.append(int(input()))

        # Insere a linha na matriz
        matriz.append(linha)

    return matriz


def maior_menor(matriz):
    # Valores iniciais
    poisic_maior = [max(matriz[0]), []]
    poisic_menor = [min(matriz[0]), []]

    # Verifica em cada linha o maior e menor elemento
    i = 0  # posição da linha
    for linha in matriz:
        # maior número da linha x
        maior_num = max(linha)
        if maior_num > poisic_maior[0]:
            poisic_maior = [maior_num, [i, linha.index(maior_num)]]
        elif maior_num == poisic_maior[0] and poisic_maior[1] == []:
            poisic_maior = [maior_num, [i, linha.index(maior_num)]]

            # menor número da linha x
        menor_num = min(linha)
        if menor_num < poisic_menor[0]:
            poisic_menor = [menor_num, [i, linha.index(menor_num)]]
        elif menor_num == poisic_menor[0] and poisic_menor[1] == []:
            poisic_menor = [menor_num, [i, linha.index(menor_num)]]

        i += 1  # muda linha

    print(tuple(poisic_maior[1]))
    print(tuple(poisic_menor[1]))


def main():
    tamanho = int(input())
    result = faz_matriz_quadrada(tamanho)
    maior_menor(result)


if __name__ == '__main__':
    main()