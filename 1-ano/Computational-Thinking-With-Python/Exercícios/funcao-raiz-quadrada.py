import math
def raiz(numero):
    raiz_quadrada = math.sqrt(numero)
    return raiz_quadrada

numero = float(input("Digite o número da raíz: "))

print(f"A raíz quadrada de {numero} é {raiz(numero):.2f}")