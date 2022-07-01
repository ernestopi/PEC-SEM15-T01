def temperaturas_list():
    temperaturas = []
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    for mes in range(12):
        temp = float(input())
        escala = input().strip().upper()

        # Converter temperatura para kelvin
        if escala == 'F':
            temp = (temp + 459.67) * (5 / 9)
            escala = 'K'
            # temperaturas.append((round(temp, 2), meses[mes]))
        elif escala == 'C':
            temp = temp + 273.15
            escala = 'K'
            # temperaturas.append((round(temp, 2), meses[mes]))

        temperaturas.append((round(temp, 2), meses[mes]))

    return temperaturas


def temp_acima_media(m, temp):
    temperaturas = []

    for valor in temp:
        if valor[0] > m:
            temperaturas.append(valor)

    return temperaturas


def temp_media(temp):
    valores = []
    for valor in temp:
        # print(valor[0])
        valores.append(valor[0])

    tam = len(valores)
    soma = sum(valores)

    return round(soma / tam, 2)


def main():
    temperaturas = temperaturas_list()
    media = temp_media(temperaturas)
    dados_result = temp_acima_media(media, temperaturas)

    print('TEMPERATURA MÉDIA ANUAL')
    print(f'{media}K')
    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')

    for valor in dados_result:
        print(f'{valor[1]}: {valor[0]}K')


if __name__ == '__main__':
    main()