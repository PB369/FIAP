# RM97937 - Pedro Henrique Fernandes Lô de Barros

from tkinter import *

def alterarImagem():
    if ballistamon.get() and shoutmon.get() and dorulumon.get():
        rotuloImagens["image"] = imagemShoutmonX5
    
    elif ballistamon.get() and dorulumon.get():
        rotuloImagens["image"] = imagemShoutmonX4

    elif ballistamon.get() and shoutmon.get():
        rotuloImagens["image"] = imagemShoutmonX2
    
    elif shoutmon.get() and dorulumon.get():
        rotuloImagens["image"] = imagemShoutmonX3
    
    elif ballistamon.get():
        rotuloImagens["image"] = imagemBallistamon

    elif dorulumon.get():
        rotuloImagens["image"] = imagemDorulumon

    elif shoutmon.get():
        rotuloImagens["image"] = imagemShoutmon

    else:
        rotuloImagens["image"] = imagemDesconhecido

fonte = ("Arial", "12", "bold")

window = Tk()
window.title("O Programa Fusão")
window.geometry("600x400")

ballistamon = BooleanVar()
dorulumon = BooleanVar()
shoutmon = BooleanVar()

container1 = Frame(window)
container2 = Frame(window, pady=35)
container1.pack(side=LEFT)
container2.pack(side=TOP)

imagemDesconhecido = PhotoImage(file="digimon/desconhecido.png")
imagemBallistamon = PhotoImage(file="digimon/ballistamon.png")
imagemDorulumon = PhotoImage(file="digimon/dorulumon.png")
imagemShoutmon = PhotoImage(file="digimon/shoutmon.png")
imagemShoutmonX2 = PhotoImage(file="digimon/shoutmonX2.png")
imagemShoutmonX3 = PhotoImage(file="digimon/shoutmonX3.png")
imagemShoutmonX4 = PhotoImage(file="digimon/shoutmonX4.png")
imagemShoutmonX5 = PhotoImage(file="digimon/shoutmonX5.png")

rotuloImagens = Label(container2)
rotuloImagens["image"] = imagemDesconhecido
rotuloImagens.grid(row=0, column=1)

checkBallistamon = Checkbutton(container1, text="Ballistamon", font=fonte, variable=ballistamon, width=15, padx=10, pady=5, anchor="w", command=alterarImagem)

checkDorulumon = Checkbutton(container1, text="Dorulumon", font=fonte, variable=dorulumon, width=15, padx=10, pady=5, anchor="w", command=alterarImagem)

checkShoutmon = Checkbutton(container1, text="Shoutmon", font=fonte, variable=shoutmon, width=15, padx=10, pady=5, anchor="w", command=alterarImagem)


checkBallistamon.grid(row=0, column=0)
checkDorulumon.grid(row=1, column=0)
checkShoutmon.grid(row=2, column=0)


window.mainloop()