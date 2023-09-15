# RM97937 - Pedro Henrique Fernandes Lô de Barros

import json
import os

print("Bem-vindo!")
login = input("Digite o seu nome de login: ")
senha = input("Digite a sua senha: ")

conjunto_usuarios = {}
if os.path.exists("usuarios.json"):
    with open("usuarios.json", "r", encoding="utf-8") as arquivo:
        conjunto_usuarios = json.loads(arquivo.read())

if login in conjunto_usuarios:
    if senha == conjunto_usuarios[login]["Senha"]:
        print("Acesso concedido!")
    else:
        print("Senha incorreta.")
else:
    print("Login inexistente.")