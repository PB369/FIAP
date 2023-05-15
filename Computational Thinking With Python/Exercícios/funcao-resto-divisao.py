def resto(n1, n2):
    resto_div = n1%n2
    return resto_div

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = resto(num1, num2)
print(f"O resto da divisão é {resultado}")