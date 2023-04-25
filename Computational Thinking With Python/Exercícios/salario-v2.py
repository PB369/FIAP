#Recebendo os dados desejados do funcionário:
salario = float(input("Digite o valor do seu salário: "))
dependentes = int(input("Digite a quantidade de dependentes que você possui: "))

#Calculando o aumento do salário e os descontos determinados:
salario_bruto = salario * 1.2
inss = salario_bruto * 0.11
imposto_renda = salario_bruto * 0.05
plano_saude = dependentes * 137.5
salario_liquido = salario_bruto - inss - imposto_renda - plano_saude

#Exibindo o salário bruto com o aumento, os descontos sobre ele e o salário líquido final:
print(f"O salário bruto com o aumento de 20% é de R${salario_bruto:.2f}.\n")
print(f"Mas foi descontado deste valor o INSS (R${inss:.2f}), o Imposto de Renda (R${imposto_renda:.2f}) e o Plano de Saúde (R${plano_saude:.2f}).\n")
print(f"Assim, seu salário líquido é de R${salario_liquido:.2f}.")