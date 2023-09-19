def ordem(lista):
    lista.sort(reverse = True)
    for i in lista:
        print(f"{i:.3f}")

lista = []
for i in range(0, 4, 1):
    numero = float(input("Digite o número desejado: "))
    lista.append(numero)
ordem(lista)