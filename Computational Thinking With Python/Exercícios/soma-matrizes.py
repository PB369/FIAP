matriz1 = []
matriz2 = []
matriz3 = []
linhas = 3
colunas = 2


for i in range(0, linhas, 1):
    valores = []
    for j in range(0 , colunas, 1):
        num = float(input("Digite um número qualquer (m1): "))
        valores.append(num)
    matriz1.append(valores[:])

for i in range(0, linhas, 1):
    valores = []
    for j in range(0 , colunas, 1):
        num = float(input("Digite um número qualquer (m2): "))
        valores.append(num)
    matriz2.append(valores[:])

for i in range(0, linhas, 1):
    soma = []
    num1 = []
    num2 = []
    num_soma = 0
    for j in range(0, colunas, 1):
        num1.append(matriz1[i][j])
        num2.append(matriz2[i][j])
        num_soma = num1[0] + num2[0]
    matriz3.append(num_soma)
print(f"A matriz resultante da soma das outras duas é esta:\n\n{matriz3}")