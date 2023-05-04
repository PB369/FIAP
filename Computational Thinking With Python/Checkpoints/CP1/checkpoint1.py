import random

resultado = vencedor = ""

# Sorteando em número e atribuindo um nome ao oponente:
oponente = random.randint(1, 3)
match oponente:
    case 1:
        oponente = "Guilherme"
    case 2:
        oponente = "Pedro"
    case 3:
        oponente = "Vinícius"

escolha_op = ""
num_oponente = random.randint(1, 5) # Sorteia o número do oponente

print("Bem-vindo ao jogo do Par ou Ímpar!\n")
# Pedindo o nome e as escolhas do jogador:
jogador = input("Digite o seu nome: ")
escolha_jg = int(input(f"Olá, {jogador}. Digite [1] para PAR ou [2] para ÍMPAR: "))
num_jogador = int(input("Digite o número de 1 a 5 que você deseja jogar: "))

# Atribuindo as strings "PAR" ou "IMPAR" ao número escolhido pelo jogador:
if escolha_jg == 1:
    escolha_jg = "PAR"
    escolha_op = "ÍMPAR"
else:
    escolha_jg = "ÍMPAR"
    escolha_op = "PAR"

# Determinando se o número final é par ou ímpar:
if (num_oponente + num_jogador)%2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

# Determinando o vencedor da partida:
if resultado == escolha_jg:
    vencedor = "você"
else:
    vencedor = oponente

# Exibindo ao jogador o resultado da partida:
print(f"\n{jogador}, você disputou contra o {oponente}. A sua escolha foi {escolha_jg} e a do seu oponente foi {escolha_op}.\nO número que você escolheu foi {num_jogador} e a de {oponente} foi {num_oponente}.\n")

print(f"De acordo com essas informações, o vencedor foi {vencedor}.")