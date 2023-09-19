peso_atual = peso_final = maior_peso = 0
while peso_final < 100000:
    peso_atual = float(input("Digite o peso do hipopótamo: "))
    peso_final += peso_atual
    if maior_peso < peso_atual:
        maior_peso = peso_atual
print(f"O maior peso foi de {maior_peso:.2f}.")