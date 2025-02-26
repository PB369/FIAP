# RM97937 - Pedro Henrique Fernandes Lô de Barros

from tkinter.ttk import *
from tkinter import *
import json
import os

def register():
    mensagem["fg"] = "black"
    mensagem["text"] = ""
    userName = str(inputName.get())
    userID = str(inputID.get())
    userPassword = str(inputSenha.get())

    user = {}
    usersData = {}

    user.update({"name": userName})
    user.update({"id": userID})
    user.update({"password": userPassword})

    if os.path.exists("usersData.json"):
        with open("usersData.json", "r") as file:
            usersData = json.loads(file.read())

    if userName != "" and userID != "" and userPassword != "":
        usersData.update({userID: user})
        mensagem["text"] = "Cadastro bem-sucedido."
        mensagem["fg"] = "green"
    else:
        mensagem["text"] = "Preencha os campos requisitados!"
        mensagem["fg"] = "red"

    with open("usersData.json", "w", encoding="utf-8") as file:
        json.dump(usersData, file)
    
def login():
    mensagem["fg"] = "black"
    mensagem["text"] = ""
    userID = str(inputID.get())
    userPassword = str(inputSenha.get())

    with open("usersData.json", "r") as file:
        usersData = json.loads(file.read())

    if userID != "" and userPassword != "":
        if userID in usersData:
            userName = usersData[userID]["name"]
            if userPassword == usersData[userID]["password"]:
                mensagem["text"] = f"Seja bem-vindo, {userName}!"
            else:
                mensagem["text"] = "Senha incorreta."
                mensagem["fg"] = "red"
        else:
            mensagem["text"] = "Usuário não encontrado."
            mensagem["fg"] = "red"
    else:
        mensagem["text"] = "Preencha os campos requisitados!"
        mensagem["fg"] = "red"

def areaCadastro():
    mensagem["fg"] = "black"
    mensagem["text"] = ""
    titulo["text"] = "Área de cadastro"
    tituloNome["text"] = "Nome: "
    tituloID["text"] = "ID: "
    tituloSenha["text"] = "Senha: "
    botaoExecutar["text"] = "Cadastrar"
    botaoExecutar["command"] = register

def areaLogin():
    tituloNome["text"] = ""
    mensagem["fg"] = "black"
    mensagem["text"] = ""
    titulo["text"] = "Área de login"
    tituloID["text"] = "ID: "
    tituloSenha["text"] = "Senha: "
    botaoExecutar["text"] = "Entrar"
    botaoExecutar["command"] = login

window = Tk()
window.title("Sistema de Registro")
window.geometry("450x450")
window.configure(background="white")

fonteTitulos = ("Arial", "20", "bold")
fonteMensagem = ("Arial", "18")

tituloWindow = Label(window, text="Bem-vindo!", font=fonteTitulos, bg="white", pady=15)
tituloWindow.pack()

containerEscolha = Frame(window, bg="white")
containerEscolha.pack()
botaoEscolhaCadastrar = Button(containerEscolha, text="Cadastrar", command=areaCadastro, bg="white")
botaoEscolhaCadastrar.pack()
botaoEscolhaLogin = Button(containerEscolha, text="Acessar", command=areaLogin, bg="white")
botaoEscolhaLogin.pack()

containerCadastroLogin = Frame(window, bg="white")
containerCadastroLogin.pack()

titulo = Label(containerCadastroLogin, text="", font=fonteTitulos, pady=30, bg="white")
titulo.pack()

tituloNome = Label(containerCadastroLogin, text="", bg="white")
tituloNome.pack()

inputName = Entry(containerCadastroLogin, bg="white")
inputName.pack()

tituloID = Label(containerCadastroLogin, text="", bg="white")
tituloID.pack()

inputID = Entry(containerCadastroLogin, bg="white")
inputID.pack()

tituloSenha = Label(containerCadastroLogin, text="", bg="white")
tituloSenha.pack()

inputSenha = Entry(containerCadastroLogin, bg="white")
inputSenha.pack()

botaoExecutar= Button(containerCadastroLogin, text="", bg="white")
botaoExecutar.pack()

mensagem = Label(containerCadastroLogin, text="", bg="white", font=fonteMensagem)
mensagem.pack()

window.mainloop()