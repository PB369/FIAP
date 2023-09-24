

import random
import csv

dica = "Filósofo"
vitoria = False
pontuacao_jogador = numero_acertos = numero_tracos = numero_rodada = iteracao = indice_jogador = 0
lista_palpites = []

# Coletando as palavras do Arquivo CSV:
lista_palavras = []
with open("palavras.csv", "r", encoding="utf-8") as arquivo:
    palavras = csv.reader(arquivo)
    for palavras_secretas in palavras:
        for palavra_secreta in palavras_secretas:
            lista_palavras.append(palavra_secreta)

# Criando o painel:
painel = [[], [], []]

indice = 0
for lista in painel:
    for letra in lista_palavras[indice]:
        lista.append("_")
    indice += 1


# Adicionando todas as letras em uma lista:
letras_palavras_lista = []
for palavra in lista_palavras:
    for letra in palavra:
        letras_palavras_lista.append(letra)


# Coletando os nomes dos 4 jogadores:
jogadores = {}
for i in range(4):
    nome = input(f"Digite o nome do {i+1}° jogador: ")
    jogadores.update({nome: 0})


lista_jogadores = []
for i in jogadores:
    lista_jogadores.append(i)


while vitoria == False:
    # Contabilizando a quantidade total de tracos no painel:
    numero_tracos = 0
    for lista in painel:
        for elemento in lista:
            if elemento == "_":
                numero_tracos += 1

    # Verificando condição de vitória:
    if numero_tracos == 0:
        print("Vocês concluíram o jogo. Parabéns!")
        print("-"*70)
        break

    numero_rodada += 1

    # Restaurando variáveis a cada quatro iterações, para não dar bug:
    pontuacao_jogador = 0
    if iteracao == 4:
      indice_jogador = 0
      iteracao = 0
    
    iteracao += 1

    # Exibindo o número da rodada, o painel e a dica:
    print("")
    print(f"Rodada {numero_rodada}\n")
    for i in painel:
        print(i)
    
    print(f"\nA dica é: '{dica}'")

    # Selecionando o jogador da rodada e girando a roda:
    jogador = lista_jogadores[indice_jogador]
    indice_jogador += 1

    girar = input(f"{jogador}, é a sua vez. Gire a roda (Digite G): ")
    while girar.lower() != "g":
        girar = input("Gira direito isso daí pô jkkkk\nDigite G:")


    # Sorteando e exibindo a opção da Roda:
    opcoes_lista = []
    with open("opcoes-roda.txt", "r", encoding="utf-8") as arquivo:
        for i in arquivo:
            opcoes_lista.append(i.strip())
    sorteio = opcoes_lista[random.randint(0, len(opcoes_lista)-1)]
    print(f"\nA roda parou nesta opção: {sorteio}")

    # Determinando os efeitos da opção sorteada:
    if sorteio == "passa-vez":
        # Exibindo as informações da jogada e pulando para a próxima rodada:
        print("\nOs seus palpites foram estes:")
        for i in lista_palpites:
            print(f"- {i}")

        print("")
        for i in jogadores:
            print(f"Nome: {i}\t| Pontuação: {jogadores[i]}")
        print("")
        print("-"*70)
        continue
    elif sorteio == "perde-tudo":
        jogadores[jogador] = 0
    else:
        # Caso para quando restarem apenas 3 letras:
        if numero_tracos == 3:
            escolha_adivinha = input("Você deseja tentar adivinhar as palavras? (S/N)\n")
            if escolha_adivinha.lower() == "s":
                lista_adivinha_palavras = []
                indice = 1
                # Recebendo os palpites de palavras do jogador:
                for palavra in lista_palavras:
                    palpite = input(f"{indice}° palavra: ")
                    indice += 1
                    lista_adivinha_palavras.append(palpite)

                # Verificando se o jogador acertou as palavras e modificando o painel:
                indice_palavra = 0
                indice_letra = 0
                for palavra in lista_adivinha_palavras:
                    indice_letra = 0
                    if palavra.lower() == lista_palavras[indice_palavra]:
                        for letra in palavra:
                            painel[indice_palavra][indice_letra] = letra.upper()
                            indice_letra += 1
                    else:
                        pontuacao_jogador = 0
                        continue
                    indice_palavra += 1


            # Realizando o palpite das letras:
            else:
                palpite = input("\nDigite o seu palpite para uma letra: ")
                if not palpite in lista_palpites:
                    indice = 0
                    lista_palpites.append(palpite)
                    for palavra in lista_palavras:
                        for letra in palavra:
                            if palpite == letra:
                                numero_acertos += 1
                                # Modificando o painel com o novo acerto:
                                indice_letra = 0
                                indice_palavra = 0
                                for palavra in lista_palavras:
                                    indice_letra = 0
                                    for letra in palavra:
                                        if letra == palpite.lower():
                                            for lista in painel:
                                                for indiceElemento in range(0, len(lista), 1):
                                                    if indiceElemento == indice_letra:
                                                        painel[indice_palavra][indice_letra] = palpite.upper()
                                        indice_letra += 1
                                    indice_palavra += 1
            
                    pontuacao_jogador += (numero_acertos * int(sorteio))
                    jogadores[jogador] = pontuacao_jogador
                    numero_acertos = 0

        # Realizando o palpite das letras:
        else:
            palpite = input("\nDigite o seu palpite para uma letra: ")
            if not palpite in lista_palpites:
                indice = 0
                lista_palpites.append(palpite)
                for palavra in lista_palavras:
                    for letra in palavra:
                        if palpite == letra:
                            numero_acertos += 1
                            # Modificando o painel com o novo acerto:
                            indice_letra = 0
                            indice_palavra = 0
                            for palavra in lista_palavras:
                                indice_letra = 0
                                for letra in palavra:
                                    if letra == palpite.lower():
                                        for lista in painel:
                                            for indiceElemento in range(0, len(lista), 1):
                                                if indiceElemento == indice_letra:
                                                    painel[indice_palavra][indice_letra] = palpite.upper()
                                    indice_letra += 1
                                indice_palavra += 1
           
                pontuacao_jogador += (numero_acertos * int(sorteio))
                jogadores[jogador] = pontuacao_jogador
                numero_acertos = 0

            else:
                print("\nVocê fez um palpite igual à tentativas anteriores. Passe a vez.")

                continue

        # Passando a pontuação para o jogador da rodada atual:
        jogadores[jogador] = pontuacao_jogador

    # Exibindo as informações da jogada:
    print("\nOs seus palpites foram estes:")
    for i in lista_palpites:
        print(f"- {i}")

    print("")
    for i in jogadores:
        print(f"Nome: {i}\t| Pontuação: {jogadores[i]}")
    print("")
    print("-"*70)