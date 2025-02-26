import math

a = float(input("Digite o valor do coeficiente a: "))
b = float(input("Digite o valor do coeficiente b: "))
c = float(input("Digite o valor do coeficiente c: "))

delta = math.pow(b, 2) - (4*a*c)

x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)

print("As raízes da equação são:")
print(f"X1 = {x1}\nX2 = {x2}")