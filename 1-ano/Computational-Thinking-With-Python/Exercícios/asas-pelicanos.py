comprimento = 1
somatoria = 0
print("[Digite 0 para finalizar]")
while comprimento != 0:
    comprimento = float(input("Digite o comprimento da asa: "))
    somatoria += comprimento
print(f"A somatória do comprimento das asas é de {somatoria:.2f}.")