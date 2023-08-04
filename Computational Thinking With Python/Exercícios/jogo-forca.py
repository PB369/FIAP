# import random

# indice_escondida = 0
# palavra_escolhida = ""
# frases = ["finge que tem, exige dos outros, mas não faz o que diz", "burro, burro, você é burro", "invariável, persistente"]
# sorteio = random.randint(0, 3)
# match sorteio:
#     case 0:
#         palavra_escolhida = "hipócrita"
#     case 1:
#         palavra_escolhida = "ignorante"
#     case 2:
#         palavra_escolhida = "constante"

# palavra_escondida = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

# print("Bem-vindo ao Jogo da Forca!")
# print("estrutura da forca")
# print(palavra_escondida)
# letra = input("Digite seu palpite de letra: ")

# for i in palavra_escolhida:
#     indice_escondida += 1
#     if letra == i:
#         palavra_escondida.pop(indice_escondida)
#         palavra_escondida.insert(indice_escondida, letra)
#     else:
#         print("Você errou!")

lista = ["_", "_", "_"]
indice = 0
letra = "e"
string = "teste"
for i in string:
    indice += 1
    if letra == i:
        lista.remove(indice)
        lista.append(letra)
print(lista)