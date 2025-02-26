import random

resultado = ""

#Sorteando a escolha do computador:
escolha_pc = random.randint(1, 3)
if escolha_pc == 1:
    escolha_pc = "Pedra"
elif escolha_pc == 2:
    escolha_pc = "Papel"
else:
    escolha_pc = "Tesoura"

#Recebendo a escolha do jogador:
escolha_jg = int(input("Digite 1 para Pedra, 2 para Papel ou 3 para Tesoura: "))

#Atribuindo palavras ao número escolhido pelo jogador:
if escolha_jg == 1:
    escolha_jg = "Pedra"
elif escolha_jg == 2:
    escolha_jg = "Papel"
else:
    escolha_jg = "Tesoura"

#Comparando as escolhas de cada um e determinando o resultado final:
if escolha_jg == escolha_pc:
    resultado = "Empate"
elif escolha_jg == "Pedra" and escolha_pc == "Tesoura":
    resultado = "Você ganhou!"
elif escolha_jg == "Papel" and escolha_pc == "Pedra":
    resultado = "Você ganhou!"
elif escolha_jg == "Tesoura" and escolha_pc == "Papel":
    resultado = "Você ganhou!"
else:
    resultado = "Você perdeu"

#Imprimindo as informações finais da rodada:
print(f"A escolha do usuário foi: {escolha_jg}")
print(f"A escolha do computador foi: {escolha_pc}")
print(resultado)