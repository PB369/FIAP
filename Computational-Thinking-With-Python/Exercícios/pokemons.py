# PEDRO HENRIQUE FERNANDES LÔ DE BARROS
# RM97937

pokemons = (["Pichu", "Luxray"], "Elétrico", ["Amaura"], "Pedra", ["Talonflame", "Slugma"], "Fogo", ["Psyduck", "Wimpod"], "Água")

escolha = input("Digite o tipo de Pokemon que você quer pesquisar: ")

if escolha.upper() == "ELÉTRICO" or escolha.upper() == "ELETRICO":
    escolha = 1
    print(f"\nQuantidade de itens: {len(pokemons[0])}\n")
    for i in pokemons[escolha-1]:
        print(f"- {i}")
elif escolha.upper() == "PEDRA":
    escolha = 3
    print(f"\nQuantidade de itens: {len(pokemons[2])}\n")
    for i in pokemons[escolha-1]:
        print(f"- {i}")
elif escolha.upper() == "FOGO":
    escolha = 5
    print(f"\nQuantidade de itens: {len(pokemons[4])}\n")
    for i in pokemons[escolha-1]:
        print(f"- {i}")
elif escolha.upper() == "ÁGUA" or escolha.upper() == "AGUA":
    escolha = 7
    print(f"\nQuantidade de itens: {len(pokemons[6])}\n")
    for i in pokemons[escolha-1]:
        print(f"- {i}")
else:
    print("Este tipo não está disponível.")