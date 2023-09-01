# RM97937 - Pedro Henrique Fernandes Lô de Barros

import random

matriz = []
linhas = 5
colunas = 5

# Criando a matriz:

for i in range(0, linhas, 1):
    valores = []
    for j in range(0 , colunas, 1):
        num = random.randint(10, 30)
        valores.append(num)
    matriz.append(valores[:])

# Somando a linha 4:

soma_linha4 = 0
for i in matriz[3]:
    soma_linha4 += i

# Somando a coluna 2:

soma_coluna2 = 0
valores_coluna = []
for i in range(len(matriz)):
    valores = []
    for j in range(0, colunas, 1):
        if j == 1:
            num = matriz[i][j]
            valores_coluna.append(num)

for i in valores_coluna:
    soma_coluna2 += i

# Somando a diagonal principal:

soma_diago_principal = 0
for i in range(len(matriz)):
    soma_diago_principal += matriz[i][i]

# Somando a diagonal secundária:

soma_diago_secundaria = 0
for i in range(len(matriz)):
    soma_diago_secundaria += matriz[i][len(matriz) - 1 - i]

# Somando todos os valores da matriz:

soma_valores_matriz = 0
soma_linha = 0
valores_linha = []
for i in range(len(matriz)):
    valores = []
    for j in range(0, colunas, 1):
        num = matriz[i][j]
        valores.append(num)
    for k in valores:
        soma_linha += k
    valores_linha.append(soma_linha)
    soma_linha = 0

for i in valores_linha:
    soma_valores_matriz += i

# Exibindo os resultados:

print("A matriz gerada é esta:\n")
for i in matriz:
    print(i)
print("\n")
print("Segue abaixo o resultado dos cálculos sobre esta matriz:\n")
print(f"Soma da linha 4: {soma_linha4}")
print(f"Soma da coluna 2: {soma_coluna2}")
print(f"Soma da diagonal principal: {soma_diago_principal}")
print(f"Soma da diagonal secundária: {soma_diago_secundaria}")
print(f"Soma de todos os valores da matriz: {soma_valores_matriz}")