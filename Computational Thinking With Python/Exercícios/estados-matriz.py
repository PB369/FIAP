matriz = []
qtdelin = 5
qtdecol = 2

print("Digite o nome e o estado de nascença de cinco pessoas:")
for i in range(0, qtdelin, 1):
    linha = []
    for j in range(0, qtdecol, 1):
        valor = input("-> ").upper()
        linha.append(valor)
    matriz.append(linha[:])
escolha_estado = input("Escolha um estado brasileiro: ").upper()
for i in range(0, len(matriz), 1):
    if escolha_estado == matriz[i][1]:
        print(matriz[i][0])