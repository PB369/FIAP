from tkinter.ttk import *
from tkinter import *
import random

def mudaForca(numImg):
    novaImagemForca = "./imagens/f" + str(numImg) + ".png"
    imagemForca["file"] = novaImagemForca

def verificaPalpite():
    global idImagemForca
    if idImagemForca <= 6:
        indice = -1
        letraPalpite = rotuloPalpiteInput.get()
        if (letraPalpite in palavra_secreta) and (not letraPalpite in listaPalpites):
            rotuloMensagem["text"] = ""
            for letra in palavra_secreta:
                indice += 1
                if letraPalpite == letra:
                    palavra_escondida[indice] = letraPalpite
                    listaPalpites.append(letraPalpite)
        elif letraPalpite in listaPalpites:
            print(listaPalpites)
            rotuloMensagem["text"] = "Você já usou esta letra. Tente outra!"
        else:
            rotuloMensagem["text"] =""
            idImagemForca += 1
            mudaForca(idImagemForca)

        rotuloPalavra["text"] = palavra_escondida
        rotuloLetras["text"] += f" {letraPalpite}"

        if not ("_" in palavra_escondida) and idImagemForca <= 6:
            rotuloMensagem["text"] = "VOCÊ VENCEU!"
    else:
        rotuloMensagem["text"] = "VOCÊ PERDEU!"
        

idImagemForca = 1
vitoria = False
palavra_escondida = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
listaPalpites = []

sorteio_palavra = random.randint(1,3)
match sorteio_palavra:
    case 1:
        palavra_secreta = "hipócrita"
    case 2:
        palavra_secreta = "ignorante"
    case 3:
        palavra_secreta = "constante"

window = Tk()
window.title("Jogo da Forca")
window.geometry("1200x500")

fonte = ("Arial", "24")

imagemForca = PhotoImage(file="./imagens/f1.png")

conteinerForca = Frame(window)
conteinerDados = Frame(window)
conteinerForca.grid(row=0, column=0)
conteinerDados.grid(row=0, column=1)

rotuloForca = Label(conteinerForca)
rotuloForca["image"] = imagemForca
rotuloForca.pack()

rotuloPalavra = Label(conteinerDados, text=palavra_escondida, font=fonte)
rotuloPalavra.pack()

conteinerPapite = Frame(conteinerDados)
conteinerPapite.pack()

rotuloPalpiteTitulo = Label(conteinerPapite, text="Digite uma letra: ", font=fonte)
rotuloPalpiteInput = Entry(conteinerPapite, font=fonte)
rotuloPalpiteTitulo.pack(side=LEFT)
rotuloPalpiteInput.pack(side=RIGHT)

rotuloLetras = Label(conteinerDados, text="Letras:", font=fonte)
botaoPalpitar = Button(conteinerDados, text="Palpitar", padx=10, pady=5, command=verificaPalpite)
rotuloLetras.pack()
botaoPalpitar.pack()

rotuloMensagem = Label(conteinerDados, text="", font=fonte)
rotuloMensagem.pack()

window.mainloop()