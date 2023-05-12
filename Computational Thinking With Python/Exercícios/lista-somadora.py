lista = []
contador = 0
soma = 0
indice_numero = 0

try:
    while contador < 15:
        indice_numero += 1
        item = int(input(f"Digite o {indice_numero}° número inteiro da lista: "))
        lista.append(item)
        contador += 1
    for i in lista:
        soma += i
    print(f"A soma destes números é {soma}")

except ValueError:
    print("O valor inserido está inválido")
finally:
    print("\nPrograma encerrado.")