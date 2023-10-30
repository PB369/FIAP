from tkinter.ttk import *
from tkinter import *
import random

tentativas = 6
vitoria = False
palavra_escondida = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

def verificaPalpite():
    indice = 0
    letraPalpite = rotuloPalpiteInput.get()
    for letra in palavra_secreta:
        indice += 1
        if letraPalpite == letra:
            palavra_escondida[indice] = letraPalpite
    indice = 0

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

imagemF1 = PhotoImage(file="./imagens/f1.png")
imagemF2 = PhotoImage(file="./imagens/f2.png")
imagemF3 = PhotoImage(file="./imagens/f3.png")
imagemF4 = PhotoImage(file="./imagens/f4.png")
imagemF5 = PhotoImage(file="./imagens/f5.png")
imagemF6 = PhotoImage(file="./imagens/f6.png")
imagemF7 = PhotoImage(file="./imagens/f7.png")

conteinerForca = Frame(window)
conteinerDados = Frame(window)
conteinerForca.grid(row=0, column=0)
conteinerDados.grid(row=0, column=1)

rotuloForca = Label(conteinerForca)
rotuloForca["image"] = imagemF1
rotuloForca.pack()

rotuloPalavra = Label(conteinerDados, text=palavra_escondida, font=fonte)
rotuloPalavra.pack()

conteinerPapite = Frame(conteinerDados)
conteinerPapite.pack()

rotuloPalpiteTitulo = Label(conteinerPapite, text="Digite uma letra: ", font=fonte)
rotuloPalpiteInput = Entry(conteinerPapite, font=fonte)
rotuloPalpiteTitulo.pack(side=LEFT)
rotuloPalpiteInput.pack(side=RIGHT)

rotuloLetras = Label(conteinerDados, text="Letras: ", font=fonte)
botaoPalpitar = Button(conteinerDados, text="Palpitar", padx=10, pady=5, command=verificaPalpite)
rotuloLetras.pack()
botaoPalpitar.pack()

window.mainloop()