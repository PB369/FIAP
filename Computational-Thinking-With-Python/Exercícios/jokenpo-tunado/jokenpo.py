import random
from tkinter.ttk import *
from tkinter import *

def mudaImagem():
    novaImagem = "jogo_img/" + escolhaJogador.get() + ".png"
    imagemJogador["file"] = novaImagem

def resultado():
    print("")

fonte = ("Arial", "12")

window = Tk()
window.title("Jokenpô Tunado")
window.geometry("850x450")
window.configure(bg="goldenrod")

escolhaJogador = StringVar()
escolhaJogador.set("pedra")

containerEscolhas = Frame(window, padx=10, bg="goldenrod")
containerJogador = Frame(window, padx=10, bg="goldenrod")
containerOponente = Frame(window, padx=10, bg="goldenrod")

containerEscolhas.pack(side=LEFT)
containerOponente.pack(side=RIGHT)
containerJogador.pack(side=RIGHT)

texto = ["Vazio", "Pedra", "Papel", "Tesoura"]
valor = ["vazio", "pedra", "papel", "tesoura"]

tituloJogador = Label(containerJogador, text="Jogador")
tituloJogador.pack(side=TOP)
tituloOponente = Label(containerOponente, text="Oponente")
tituloOponente.pack(side=TOP)

radioPedra = Radiobutton(containerEscolhas, text="Vazio", value="pedra", variable=escolhaJogador, width=15, anchor="w", padx=10, pady=5, bg="goldenrod", font=fonte, command=mudaImagem)

for i in range(1, 4, 1):
    Radiobutton(containerEscolhas, text=texto[i], value=valor[i], indicatoron=False, variable=escolhaJogador, width=15, anchor="w", padx=10, pady=5, bg="white", font=fonte, command=mudaImagem).pack()

imagemJogador = PhotoImage(file="jogo_img/pedra.png")
rotuloJogador = Label(containerJogador, image=imagemJogador, bg="goldenrod")
rotuloJogador.pack()

imagemOponente = PhotoImage(file="jogo_img/vazio.png")
rotuloOponente = Label(containerOponente, image=imagemOponente, bg="goldenrod")
rotuloOponente.pack()

botaoJogarOn = StringVar()
botaoJogarOff = StringVar()
radioJogar = Radiobutton(containerJogador, text="Jogar", value="jogar", indicatoron=False, variable=botaoJogarOff, width=15, anchor="w", padx=10, pady=5, bg="white", font=fonte, command=resultado).pack(side=BOTTOM)

window.mainloop()