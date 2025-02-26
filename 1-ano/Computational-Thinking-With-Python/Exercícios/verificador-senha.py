senha = "p4ssw0rd"
tentativa = ""
while tentativa != "p4ssw0rd":
    tentativa = input("Digite a sua senha: ")
    if tentativa != senha:
        print("Senha inválida. Tente novamente.")
print("Acesso concedido.")