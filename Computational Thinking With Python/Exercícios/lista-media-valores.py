lista = []
contador = 0
soma = 0
indice_numero = 0

try:
    for i in range(20):
        indice_numero += 1
        item = float(input(f"Digite o {indice_numero}° número da lista: "))
        lista.append(item)
    for i in lista:
        soma += i
    media = (soma)/len(lista)
    print(f"A média destes números é {media}")

except ValueError:
    print("O valor inserido está inválido")
finally:
    print("\nPrograma encerrado.")