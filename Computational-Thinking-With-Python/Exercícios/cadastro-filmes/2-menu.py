# RM97937 - Pedro Henrique Fernandes Lô de Barros

import csv

escolha = input("Escolha uma das opções abaixo para perquisar seu filme:\n-Título\n-Diretor\n-Gênero\n\n-> ")
info_escolha = ""
info_escolha = input("-> ")

with open('filmes.csv', 'r', encoding='utf-8') as arquivo:
    filmes = csv.reader(arquivo)
    next(filmes)
    filme_encontrado = False
    for i in filmes:
        if info_escolha in i:
            print(i)
            filme_encontrado = True

    if not filme_encontrado == True:
        print("Nenhum filme corresponde à sua pesquisa.")