import random
import csv

dica = "Filósofo"
vitoria = False
pontuacao_jogador = 0
numero_acertos = 0
lista_palpites = []

while vitoria == False:
    # Coletando os nomes dos 4 jogadores:
    jogadores = []
    for i in range(4):
        nome = input(f"Digite o nome do {i+1}° jogador: ")
        jogadores.append(nome)

    # Sorteando o jogador da rodada:
    jogador = jogadores[random.randint(0, 3)]

    # Exibindo painel e a dica:
    print(f"Os Jogadores da Roda a Roda são estes:")
    for i in jogadores:
        print(f"- {i}")
    print(f"A dica é {dica}")

    # Girando a roda:
    girar = ""
    while girar.lower() != "g":
        girar = input(f"{jogador}, você foi escolhido. Gire a roda (Digite G): ")
        print("Gira direito isso daí pô jkkkk")

    # Sorteando opção da Roda:
    opcoes_lista = []
    with open("opcoes-roda.txt", "r", encoding="utf-8") as arquivo:
        for i in arquivo:
            opcoes_lista.append(i.strip())
    sorteio = opcoes_lista[random.randint(0, len(opcoes_lista)-1)]

    if sorteio == "passa-vez":
        continue
    elif sorteio == "perde-tudo":
        pontuacao_jogador = 0
    else:
        pontuacao_roda = sorteio
        palpite = input("Digite o seu palpite: ")
        lista_palpites.append(palpite)
        if not palpite in lista_palpites:
            with open("palavras.csv", "r", encoding="utf-8") as arquivo:
                palavras = csv.reader(arquivo)
                for i in palavras:
                    for j in i:
                        for k in j:
                            if palpite == k:
                                numero_acertos += 1
                pontuacao_jogador += numero_acertos * sorteio
                numero_acertos = 0