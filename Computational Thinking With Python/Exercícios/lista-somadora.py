lista = []
contador = 0
soma = 0
indice_numero = 0

try:
    for i in range(15):
        indice_numero +=1
        item = int(input(f"Digite o {indice_numero}° número inteiro da lista: "))
        lista.append(item)
    for i in lista:
        soma += i
    print(f"A soma destes números é {soma}")

except ValueError:
    print("O valor inserido é inválido")
finally:
    print("\nPrograma encerrado.")