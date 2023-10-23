from tkinter import *

def verificaPertences():
    mensagem = "Seus Pertences:"
    if tv.get():
        mensagem += "\n" + checkTv["text"]
    if pc.get():
        mensagem += "\n" + checkPc["text"]
    if vg.get():
        mensagem += "\n" + checkVg["text"]
    if bk.get():
        mensagem += "\n" + checkBk["text"]
    rotulo1["text"] = mensagem

fonte = ("Arial", "12")

window = Tk()
window.title("Pesquisa")
window.geometry("400x200")

tv = BooleanVar()
pc = BooleanVar()
vg = BooleanVar()
bk = BooleanVar()

container1 = Frame(window)
container2 = Frame(window)
container1.pack(side=LEFT)
container2.pack(side=TOP)

checkTv = Checkbutton(container1, text="Televisão", font=fonte, variable=tv, width=15, padx=10, pady=5, anchor="w", command=verificaPertences)
checkPc = Checkbutton(container1, text="Computador", font=fonte, variable=pc, width=15, padx=10, pady=5, anchor="w", command=verificaPertences)
checkVg = Checkbutton(container1, text="Video Game", font=fonte, variable=vg, width=15, padx=10, pady=5, anchor="w", command=verificaPertences)
checkBk = Checkbutton(container1, text="Bicicleta", font=fonte, variable=bk, width=15, padx=10, pady=5, anchor="w", command=verificaPertences)

checkTv.grid(row=0, column=0)
checkPc.grid(row=1, column=0)
checkVg.grid(row=2, column=0)
checkBk.grid(row=3, column=0)

rotulo1 = Label(container2, text="Seus Pertences:", pady=20)
rotulo1["font"] = "Arial 14 bold"
rotulo1.grid(row=0, column=1)

window.mainloop()