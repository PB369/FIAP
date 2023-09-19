pessoas = int(input("Digite a quantidade de pessoas que estão à mesa: "))
tulipas = int(input("Digite a quantidade de tulipas pedidas: "))
pizzas = int(input("Digite a quantidade de pizzas grandes pedidas: "))
coberturas = int(input("Digite a quantidade total de coberturas para as pizzas: "))

preco = (tulipas * 19.8) + (pizzas * 49.0) + (coberturas * 2.5)
gorjeta = preco * 0.1
conta = preco + gorjeta

print(f"\nTotal gasto: R${preco:.2f}\nValor da Gorjeta: R${gorjeta:.2f}\nSubtotal: R${conta:.2f}\n\nCada um deverá pagar R${(conta/pessoas):.2f}")