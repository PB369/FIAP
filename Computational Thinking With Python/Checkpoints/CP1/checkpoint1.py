import random

resultado = vencedor = ""

oponente = random.randint(1, 3)
match oponente:
    case 1:
        oponente = "Guilherme"
    case 2:
        oponente = "Pedro"
    case 3:
        oponente = "Vinícius"

escolha_op = ""
num_oponente = random.randint(1, 5)

print("Bem-vindo ao jogo do Par ou Ímpar!\n")
jogador = input("Digite o seu nome: ")
escolha_jg = int(input(f"Olá, {jogador}. Digite [1] para PAR ou [2] para ÍMPAR: "))
num_jogador = int(input("Digite o número de 1 a 5 que você deseja jogar: "))

if escolha_jg == 1:
    escolha_jg = "PAR"
    escolha_op = "ÍMPAR"
else:
    escolha_jg = "ÍMPAR"
    escolha_op = "PAR"

if (num_oponente + num_jogador)%2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

if resultado == escolha_jg:
    vencedor = "você"
else:
    vencedor = oponente

print(f"\n{jogador}, você disputou contra o {oponente}. A sua escolha foi {escolha_jg} e a do seu oponente foi {escolha_op}.\nO número que você escolheu foi {num_jogador} e a de {oponente} foi {num_oponente}.\n")

print(f"De acordo com essas informações, o vencedor foi {vencedor}.")