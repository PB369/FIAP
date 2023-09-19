import re

carta = {
    "nome": "Cell",
    "ki": 7400,
    "técnicas": 6000,
    "velocidade": 66,
    "transformações": 3
}

chave = input("Digite o nome da nova característica: ")
valor = input("Digite o valor desta característica: ")

carta.update({chave.lower(): valor.lower()})

indice = 1
for i in carta.keys():
    print(f"\n{indice}° Característica: {i.upper()}")
    indice += 1

escolha = input("\nEscolha uma característica desta carta: ")
if not escolha.lower() in carta:
    print("Esta característica não se encontra na carta apresentada.")
else:
    print(f"A sua escolha foi: {escolha.upper()}")
    print(f"O valor desta característica escolhida é: {carta.get(escolha.lower())}")