lista = []
quantidade_negativos = 0
quantidade_primos = 0
numero = 1

try:
    print("Digite 0 para finalizar a adição dos itens.\n")
    while numero != 0:
        numero = float(input("Digite o número desejado: "))

        if numero != 0:
            lista.append(numero)

        if numero < 0:
            quantidade_negativos += 1

        if numero == 2 or numero == 3 or numero == 5 or numero == 7:
            quantidade_primos +=1
        else:
            div1 = numero%2
            div2 = numero%3
            div3 = numero%5
            div4 = numero%7

            if div1 and div2 and div3 and div4 != 0:
                quantidade_primos += 1
    
    lista.sort()

    print("\nInformações sobre a lista gerada:\n")
    print("Tamanho da lista:", len(lista))
    print(f"A lista em ordem crescente: {lista}")
    print(f"Quantidade de números negativos: {quantidade_negativos}")
    print(f"Quantidade de números primos: {quantidade_primos}")
except ValueError:
    print("O campo só pode receber números.")
finally:
    print("\nPrograma finalizado.")