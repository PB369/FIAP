qi = 0
genios = 0
try:
    print("Digite 0 para finalizar o programa.")
    while True:
        qi = int(input("Digite o valor do QI: "))
        if qi == 0:
            break
        if qi < 140:
            continue
        genios += 1
    print(f"A quantidade de gênios é {genios}.")
except ValueError:
    print("O programa só aceita números inteiros.")