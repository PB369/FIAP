# import random

# tentativas = 6
# indice = 0
# vitoria = False

# sorteio_palavra = random.randint(1,3)
# match sorteio_palavra:
#     case 1:
#         palavra_secreta = "hipócrita"
#         dica = "Finge que tem, exige dos outros, mas não faz o que fala"
#     case 2:
#         palavra_secreta = "ignorante"
#         dica = "Burro, burro, você é burro!"
#     case 3:
#         palavra_secreta = "constante"
#         dica = "Permanece firme; não muda"

# print(palavra_secreta)

# print("Bem-vindo ao Jogo da Forca!\n")

# forca_original = """
# ----------
#          |"""

# cabeca_corpo = "\t O"
# tronco_corpo = "|"
# bra_dir_corpo = "\ "
# bra_esq_corpo = "\t/"
# perna_dir_corpo = " \ "
# perna_esq_corpo = "\t/"

# corpo = [perna_esq_corpo, perna_dir_corpo, bra_esq_corpo, bra_dir_corpo, tronco_corpo, cabeca_corpo]

# palavra_escondida = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

# print(f"\nTentativas Restantes: {tentativas}\n")
# print(f"Dica: '{dica}'")

# while not tentativas == 0:
#     letra = input("Digite o seu palpite: \n")
#     if not (letra in palavra_secreta):
#         print("\nVocê errou! Tente de novo...\n")
#         tentativas -= 1
#         print(f"\nTentativas Restantes: {tentativas}\n")
#     else:
#         for i in palavra_secreta:
#             if letra == i:
#                 palavra_escondida[indice] = letra
#             indice += 1
#         for i in palavra_escondida:
#             print(i, end=" ")
#     indice = 0

#     if not ("_" in palavra_escondida) and tentativas > 0:
#         vitoria = True
#         break

# if vitoria == True:
#     print(f"\nParabéns! Você acertou a palavra secreta: {palavra_secreta}.")
# else:
#     print(f"\nVocê perdeu. A palavra secreta era '{palavra_secreta}'.")

# Forca segundo o professor:

import random

topo =   "UU=====U"
corda =  "||     |"
cabeca = "||      "
corpo =  "||      "
pernas = "||      "
base1 =  "||"
base2 =  "||"

dica = ""
l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = l9 = "_"
palpites = ""
erro = acerto = 0
palavras = ["BATRANGUE", "AEROPORTO", "CONSELHOS"]
dicas = ["Morcego que vai e volta", "Local onde podemos viajar", "Se fosse bons, não eram de graça"]

sorteio = random.randint(0, 2)
sorteado = palavras[sorteio]
palavra = []
for i in range(0, 9, 1):
    palavra.append(sorteado[i:i+1])
dica = dicas[sorteio]

while(acerto < 9 and erro < 6):
    print()
    print()
    print(dica)
    print()
    print(topo)
    print(corda)
    print(cabeca)
    print(corpo)
    print(pernas)
    print(base1)
    print(base2)
    print(" ", l1, l2, l3, l4, l5, l6, l7, l8, l9)
    print()
    print(palpites)
    print()
    letra = input("Digite uma letra: ").upper()
    print()
    print()
    print()
    palpites += " " + letra

    if letra in palavra:
        if letra == palavra[0]:
            l1 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[1]:
            l2 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[2]:
            l3 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[3]:
            l4 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[4]:
            l5 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[5]:
            l6 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[6]:
            l7 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[7]:
            l8 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[8]:
            l9 = letra
            palavra[0] = "@"
            acerto += 1
    else:
        erro += 1
    
    if erro == 1:
        cabeca = "||     O"
    elif erro == 2:
        corpo = "||     |"
    elif erro == 3:
        corpo = "||    /|"
    elif erro == 4:
        corpo = "||    /|\ "
    elif erro == 5:
        pernas = "||    / "
    elif erro == 6:
        pernas = "||    / \ "

print()
print()
print(dica)
print()
print(topo)
print(corda)
print(cabeca)
print(corpo)
print(pernas)
print(base1)
print(base2)
print(" ", l1, l2, l3, l4, l5, l6, l7, l8, l9)
print()
print(palpites)

if acerto >= 9:
    print("Você acertou!")
else:
    print("Você errou!")
