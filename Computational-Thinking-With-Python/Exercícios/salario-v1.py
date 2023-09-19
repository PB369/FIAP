salario = float(input("Digite o valor do seu salário: "))
tempo = int(input("Digite seu tempo de trabalho em anos: "))
if tempo < 5:
    salario *= 1.05 #Atribui um aumento de 5% ao salário
elif tempo >=5 and tempo <=10:
    salario *= 1.10 #Atribui um aumento de 10% ao salário
elif tempo >= 11 and tempo <=15:
    salario *= 1.15 #Atribui um aumento de 15% ao salário
elif tempo >= 16:
    salario *= 1.20 #Atribui um aumento de 20% ao salário

print(f"O novo salário é de {salario}")