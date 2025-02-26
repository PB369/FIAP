# Pedro Henrique Fernandes Lô de Barros

from tkinter.ttk import *
from tkinter import *
import random

# Alterando a imagem da forca:
def mudaForca(numImg):
    novaImagemForca = "./imagens/f" + str(numImg) + ".png"
    imagemForca["file"] = novaImagemForca

# Verificando o palpite do usuário:
def verificaPalpite():
    global idImagemForca
    global vitoria
    if vitoria == False:
        if idImagemForca < 6:
            indice = -1
            letraPalpite = rotuloPalpiteInput.get().lower()

            # Verificando se o palpite não foi repetido:
            if not (letraPalpite in listaPalpites):
                listaPalpites.append(letraPalpite)
                # Verificando se o usuário acertou:
                if letraPalpite in palavra_secreta:
                    rotuloMensagem["text"] = ""
                    for letra in palavra_secreta:
                        indice += 1
                        if letraPalpite == letra:
                            palavra_escondida[indice] = letraPalpite
                else:
                    rotuloMensagem["text"] =""
                    idImagemForca += 1
                    mudaForca(idImagemForca)
            else:
                print(listaPalpites)
                rotuloMensagem["text"] = "Você já usou esta letra. Tente outra!"

            # Atualizando os traços e as letras testadas:
            rotuloPalavra["text"] = palavra_escondida
            rotuloLetras["text"] += f" {letraPalpite}"

            # Condição de vitória:
            if not ("_" in palavra_escondida) and idImagemForca <= 6:
                rotuloMensagem["text"] = "VOCÊ VENCEU!"
                vitoria = True
        # Condição de derrota:
        elif idImagemForca == 6:
            idImagemForca += 1
            mudaForca(idImagemForca)
            rotuloMensagem["text"] = "VOCÊ PERDEU!"

# Inicializando variáveis necessárias:
idImagemForca = 1
vitoria = False
palavra_escondida = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
listaPalpites = []

# Sorteando a palavra secreta:
sorteio_palavra = random.randint(1,3)
match sorteio_palavra:
    case 1:
        palavra_secreta = "hipócrita"
    case 2:
        palavra_secreta = "ignorante"
    case 3:
        palavra_secreta = "constante"

# Configurando a GUI:
window = Tk()
window.title("Jogo da Forca")
window.geometry("820x500")
window.configure(bg="lightblue")

fonte = ("Arial", "24")

imagemForca = PhotoImage(file="./imagens/f1.png")

conteinerForca = Frame(window, padx=20, bg="lightblue")
conteinerDados = Frame(window, padx=20, bg="lightblue")
conteinerForca.pack(side=LEFT)
conteinerDados.pack(side=RIGHT)

rotuloForca = Label(conteinerForca, bg="lightblue")
rotuloForca["image"] = imagemForca
rotuloForca.pack()

rotuloPalavra = Label(conteinerDados, text=palavra_escondida, font=fonte, pady=10, bg="lightblue")
rotuloPalavra.pack()

conteinerPapite = Frame(conteinerDados, bg="lightblue")
conteinerPapite.pack()

rotuloPalpiteTitulo = Label(conteinerPapite, text="Digite uma letra: ", font=fonte, pady=10, bg="lightblue")
rotuloPalpiteInput = Entry(conteinerPapite, font=fonte)
rotuloPalpiteTitulo.pack(side=LEFT)
rotuloPalpiteInput.pack(side=RIGHT)

rotuloLetras = Label(conteinerDados, text="Letras:", font=fonte, pady=10, bg="lightblue")
botaoPalpitar = Button(conteinerDados, text="Palpitar", padx=10, pady=5, command=verificaPalpite)
rotuloLetras.pack()
botaoPalpitar.pack()

rotuloMensagem = Label(conteinerDados, text="", font=fonte, bg="lightblue")
rotuloMensagem.pack()

window.mainloop()