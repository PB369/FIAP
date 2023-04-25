preco = float(input("Digite o valor a ser pago: "))
pagamento = float(input("Digite o valor que foi pago: "))
troco = pagamento - preco

nota_50 = nota_20 = nota_10 = nota_5 = moeda_1 = 0

while troco != 0:
    if troco >= 50:
        nota_50 = nota_50 + (troco // 50)
        troco = troco - (50 * nota_50)
    elif troco >= 20:
        nota_20 += (troco // 20)
        troco -= (20 * nota_20)
    elif troco >= 10:
        nota_10 += (troco // 10)
        troco -= (10 * nota_10)
    elif troco >= 5:
        nota_5 += (troco // 5)
        troco -= (5 * nota_5)
    elif troco <= 5:
        moeda_1 += (troco // 1)
        troco -= (1 * moeda_1)

print("\nA quantidade de notas e moedas a serem dadas de troco são:\n")
print(f"Notas de 50: {nota_50}")
print(f"Notas de 20: {nota_20}")
print(f"Notas de 10: {nota_10}")
print(f"Notas de 5: {nota_5}")
print(f"Moedas de 1: {moeda_1}")
