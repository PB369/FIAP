#RM97937 - Pedro Henrique Fernandes Lô de Barros

from tkinter import *

def somar():
    resultado["text"] = int(caixaTxt1.get()) + int(caixaTxt2.get())

janela = Tk()
janela.title("Soma de Números")
titulo = Label(janela, text="Digite números nos campos abaixo: ", font="Arial 20 bold", pady=10)
titulo.pack()
container1 = Frame(janela, padx=15, pady=15)
container1.pack()
container2 = Frame(janela, padx=15, pady=15)
container2.pack()
campoTexto1 = Label(container1, text="N1: ", font="Arial 16 bold", pady=10)
campoTexto1.pack(side=LEFT)
caixaTxt1 = Entry(container1, font="Arial 16")
caixaTxt1.pack(side=RIGHT)
campoTexto2 = Label(container2, text="N2: ", font="Arial 16 bold", pady=10)
campoTexto2.pack(side=LEFT)
caixaTxt2 = Entry(container2, font="Arial 16")
caixaTxt2.pack(side=RIGHT)
botao = Button(janela, text="Calcular", padx=10, pady=5, bg="black", fg="white", font="Arial 18 bold")
botao["command"] = somar
botao.pack()
containerRs = Frame(janela, padx=15, pady=15)
containerRs.pack()
resultadoTxt = Label(containerRs, text="Resultado: ", font="Arial 16", pady=10)
resultadoTxt.pack(side=LEFT)
resultado = Label(containerRs, font="Arial 16", pady=10)
resultado.pack(side=RIGHT)
janela.mainloop()