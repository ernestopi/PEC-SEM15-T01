matriz = []
n = int(input('Insira o numero de linhas: ').strip())
m = int(input('Insira o numero de colunas: ').strip())

s = 0
#cria a matriz
for i in range(n):
    lista=[]
    for c in range(m):
        e = int(input('Insira um numero: ').strip())
        lista.append(e)
        s+=e
    matriz.append(lista)


#soma as linhas
soma_l = 0
for c in range(m):
    soma_l+=matriz[0][c]

#soma as colunas
soma_c = 0
for i in range(n):
    soma_c += matriz[i][m-1]
#A media dos numeros
media = round((s/(n*m)),4)

#maior e menor numero
q = maior = menor = 0
for linha in matriz:
    for ele in linha:
        q+=1
        if q==1:
            maior=menor=ele
        else:
            if ele>maior:
                maior=ele
            if ele <menor:
                menor=ele
tupla=soma_l,soma_c,media,menor,maior
print(tupla)

