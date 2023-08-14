# PEDRO HENRIQUE FERNANDES LÔ DE BARROS
# RM97937

tipo = 0
comparador = 0
maior_num = 0
conjunto = {0}
conjunto.remove(0)


while not tipo == 1 and not tipo == 2:
    try:
        tipo = int(input("Qual tipo numérico você quer?\n\n1 - Real\n2 - Inteiro\n\n-> "))
        if not tipo == 1 and not tipo == 2:
            raise ValueError
    except ValueError:
        print("Escolha inválida.")

if tipo == 1:
    tipo = "Real"
elif tipo == 2:
    tipo = "Inteiro"

while len(conjunto) < 10:
    try:
        if tipo == "Real":
            num = float(input(f"Digite um número do tipo {tipo}: "))
            conjunto.add(num)
        elif tipo == "Inteiro":
            num = int(input(f"Digite um número do tipo {tipo}: "))
            conjunto.add(num)

    except ValueError:
        print(f"Valor inserido não corresponde ao tipo numérico escolhido ({tipo}).")
        

for i in conjunto:
    if i >= maior_num:
        maior_num = i

print(f"\nTipo Numérico Escolhido: {tipo}")
print(f"Maior Número: {maior_num:.2f}")
print("\nSegue os todos os valores armazenados:\n")
for i in conjunto:
    print(i)
print(f"\nQuantidade de números armazenados: {len(conjunto)}")