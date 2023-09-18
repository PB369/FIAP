# RM97937 - Pedro Henrique Fernandes Lô de Barros

import csv

infos = ['Título', 'Gênero', 'Tempo de Duração', 'Nível de Censura', 'Diretor']
condicao = True
filmes = []

while condicao == True:
    lista_dados = []
    for i in infos:
        dados = input(f"Informe o {i} do filme: ")
        lista_dados.append(dados)
    filmes.append(lista_dados)
    continuar = input("Você deseja continuar cadastrando novos filmes? (S/N)\n")
    if continuar.lower() == 'n':
        condicao = False

with open('filmes.csv', 'a', encoding='utf-8', newline='') as arquivo:
    escreve_filme = csv.writer(arquivo)
    escreve_filme.writerow(infos)
    for i in filmes:
        escreve_filme.writerow(i)