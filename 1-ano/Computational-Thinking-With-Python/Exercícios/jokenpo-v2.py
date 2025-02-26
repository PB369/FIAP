import random

finalizador = "S"
rodada = vitorias_pc = vitorias_jg = 0
while finalizador != "N": #Determina uma repetição sem fim das rodadas
    resultado = ""

    #Sorteando a escolha do computador:
    escolha_pc = random.randint(1, 3)
    if escolha_pc == 1:
        escolha_pc = "Pedra"
    elif escolha_pc == 2:
        escolha_pc = "Papel"
    else:
        escolha_pc = "Tesoura"

    rodada += 1
    print(f"Rodada {rodada}\n") #Exibe o número da rodada

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
        vitorias_jg += 1
    elif escolha_jg == "Papel" and escolha_pc == "Pedra":
        resultado = "Você ganhou!"
        vitorias_jg += 1
    elif escolha_jg == "Tesoura" and escolha_pc == "Papel":
        resultado = "Você ganhou!"
        vitorias_jg += 1
    else:
        resultado = "Você perdeu"
        vitorias_pc += 1

    #Imprimindo as informações finais da rodada:
    print(f"A escolha do usuário foi: {escolha_jg}")
    print(f"A escolha do computador foi: {escolha_pc}")
    print(resultado)
    
    finalizador = input("\nVocê deseja continuar? (S/N)\n").upper()

print(f"\nQuantidade de Vitórias Totais\nPC: {vitorias_pc}\nVocê: {vitorias_jg}")