maior = medio = menor = 0
print("Escolha uma das opções abaixo:")
print("1 - Números em ordem crescente\n2 - Números em ordem decrescente\n3 - Maior número entre os demais")
i = int(input("-> "))
if i >= 1 and i <= 3:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))

    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c

    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c

    medio = a
    if b > a and c > b:
        medio = b
    if c > a and b > c:
        medio = c

    if i == 1:
        print(f"\nResultado: {menor}, {medio}, {maior}")
    elif i == 2:
        print(f"\n\nResultado: {maior}, {medio}, {menor}")
    elif i == 3:
        print(f"\nResultado: {menor}, {maior}, {medio}")
else:
    print("\nA sua escolha foi invália. Tente novamente.")