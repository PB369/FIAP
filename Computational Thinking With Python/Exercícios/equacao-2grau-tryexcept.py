import math

try:
    a = int(input("Digite o valor do coeficiente a: "))
    b = int(input("Digite o valor do coeficiente b: "))
    c = int(input("Digite o valor do coeficiente c: "))

    try:
        delta = math.pow(b, 2) - (4*a*c)
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)

        print("As raízes da equação são:")
        print(f"X1 = {x1:.2f}\nX2 = {x2:.2f}")

    except ValueError:
        print("A raíz de delta é negativa. Impossível encontrar os coeficientes X1 e X2.")

except ValueError:
    print("Erro: Os valores de a, b e c devem ser somente números inteiros.")
