import random

tentativas = 6
indice = 0
vitoria = False

sorteio_palavra = random.randint(1,3)
match sorteio_palavra:
    case 1:
        palavra_secreta = "hipócrita"
        dica = "Finge que tem, exige dos outros, mas não faz o que fala"
    case 2:
        palavra_secreta = "ignorante"
        dica = "Burro, burro, você é burro!"
    case 3:
        palavra_secreta = "constante"
        dica = "Permanece firme; não muda"

print(palavra_secreta)

print("Bem-vindo ao Jogo da Forca!\n")

forca_original = """
----------
         |"""

cabeca_corpo = "\t O"
tronco_corpo = "|"
bra_dir_corpo = "\ "
bra_esq_corpo = "\t/"
perna_dir_corpo = " \ "
perna_esq_corpo = "\t/"

corpo = [perna_esq_corpo, perna_dir_corpo, bra_esq_corpo, bra_dir_corpo, tronco_corpo, cabeca_corpo]

palavra_escondida = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

print(f"\nTentativas Restantes: {tentativas}\n")
print(f"Dica: '{dica}'")

while not tentativas == 0:
    letra = input("Digite o seu palpite: \n")
    if not (letra in palavra_secreta):
        print("\nVocê errou! Tente de novo...\n")
        tentativas -= 1
        print(f"\nTentativas Restantes: {tentativas}\n")
    else:
        for i in palavra_secreta:
            if letra == i:
                palavra_escondida[indice] = letra
            indice += 1
        for i in palavra_escondida:
            print(i, end=" ")
    indice = 0

    if not ("_" in palavra_escondida) and tentativas > 0:
        vitoria = True
        break

if vitoria == True:
    print(f"\nParabéns! Você acertou a palavra secreta: {palavra_secreta}.")
else:
    print(f"\nVocê perdeu. A palavra secreta era '{palavra_secreta}'.")
