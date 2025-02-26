print("Para retângulo:")
largura_retangulo = float(input("Digite a largura do retângulo: "))
altura_retangulo = float(input("Digite a altura do retângulo: "))
area_retangulo = largura_retangulo*altura_retangulo
print(f"A área do retângulo é de {area_retangulo}")

print("Para triângulo:")
base_triangulo = float(input("Digite a base do triângulo: "))
altura_triangulo = float(input("Digite a altura do triângulo: "))
area_triangulo = (base_triangulo*altura_triangulo)/2
print(f"A área do triângulo é de {area_triangulo}")

print("Para o trapézio:")
base_maior = float(input("Digite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura_trapézio = float(input("Digite a altura do trapézio: "))
area_trapézio = ((base_maior*base_menor)*altura_trapézio)/2
print(f"A área do trapézio é de {area_trapézio}")