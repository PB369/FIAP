from tkinter.ttk import *
from tkinter import *

def fazerPedido():
    novaImagemLanche = "cardapio/" + lanche.get() + ".png"
    imagemLanche["file"] = novaImagemLanche
    rotuloPrecoValor["text"] = precosLanche[float(lanche.get())] + precosPorcao[float(porcao.get())] + precosBebida[float(bebida.get())]

    novaImagemPorcao = "cardapio/" + porcao.get() + ".png"
    imagemPorcao["file"] = novaImagemPorcao


    novaImagemBebida = "cardapio/" + bebida.get() + ".png"
    imagemBebida["file"] = novaImagemBebida


fonte = ("Arial", "16")

window = Tk()
window.title("Lanchonete")
window.geometry("600x600")

rotuloTitulo = Label(window, text="Faça seu pedido", pady=20, font=fonte)
rotuloTitulo.pack()

containerOpcoes = Frame(window)
containerOpcoes.pack()

precosLanche = {
    "escolha": 0,
    "burguer": 34.9,
    "noodles": 44.5,
    "pizza": 49
}
rotuloLanche = Label(containerOpcoes, text="Lanche: ")
rotuloLanche.pack()
lanche = Combobox(containerOpcoes)
lanche["values"] = ("escolha", "burger", "noodles", "pizza")
lanche["state"] = "readonly"
lanche.current(0)
lanche.pack()

precosPorcao = {
    "escolha": 0,
    "fritas": 14.9,
    "nuggets": 9.5,
    "mlho": 12.3
}
rotuloPorcao = Label(containerOpcoes, text="Porção: ")
rotuloPorcao.pack()
porcao = Combobox(containerOpcoes)
porcao["values"] = ("escolha", "fritas", "nuggets", "milho")
porcao["state"] = "readonly"
porcao.current(0)
porcao.pack()

precosBebida = {
    "escolha": 0,
    "suco": 14.9,
    "shake": 19.9,
}
rotuloBebida = Label(containerOpcoes, text="Bebida: ")
rotuloBebida.pack()
bebida = Combobox(containerOpcoes)
bebida["values"] = ("escolha", "suco", "shake")
bebida["state"] = "readonly"
bebida.current(0)
bebida.pack()

conteinerImg = Frame(window)
conteinerImg.pack(pady=20)

imagemLanche = PhotoImage(file="cardapio/escolha.png")
rotuloImgL = Label(conteinerImg, image=imagemLanche)
rotuloImgL.pack(side=LEFT)

imagemPorcao = PhotoImage(file="cardapio/escolha.png")
rotuloImgP = Label(conteinerImg, image=imagemPorcao)
rotuloImgP.pack(side=RIGHT)

imagemBebida = PhotoImage(file="cardapio/escolha.png")
rotuloImgB = Label(conteinerImg, image=imagemBebida)
rotuloImgB.pack(side=RIGHT)

botao = Button(window, text="Finalizar Pedido", pady=5, padx=10, font=fonte)
botao["command"] = fazerPedido
botao.pack()

rotuloPreco = Label(window, text="Total: R$", font=fonte, pady=10)
rotuloPreco.pack(side=LEFT)

rotuloPrecoValor = Label(window, text="", font=fonte, pady=10)
rotuloPrecoValor.pack(side=RIGHT)

window.mainloop()