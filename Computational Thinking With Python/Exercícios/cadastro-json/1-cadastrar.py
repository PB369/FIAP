# RM97937 - Pedro Henrique Fernandes Lô de Barros

import json

try:
    condicao = True
    conjunto_usuarios = {}
    while not condicao == False:
        usuario = {}

        nome = input("Digite o seu nome de usuário: ")
        login = input("Digite o seu nome para o login: ")
        senha = input("Digite uma senha para a sua conta: ")

        usuario.update({"Nome": nome})
        usuario.update({"Login": login})
        usuario.update({"Senha": senha})

        conjunto_usuarios.update({login: usuario})
        print(conjunto_usuarios)

        continuar = input("Você deseja cadastrar um novo usuário? (S/N)\n")
        if continuar.lower() == "n":
            with open("usuarios.json", "a", encoding="utf-8") as arquivo:
                json.dump(conjunto_usuarios, arquivo)
            break

except ValueError:
    print("Error")