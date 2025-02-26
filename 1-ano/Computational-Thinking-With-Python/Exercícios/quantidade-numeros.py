numero = 1
somatoria = 0
print("[Digite zero para finalizar a contagem]")
while numero != 0:
    numero = float(input("Digite um número: "))
    somatoria += 1
print(f"Foram digitados {somatoria - 1} números")