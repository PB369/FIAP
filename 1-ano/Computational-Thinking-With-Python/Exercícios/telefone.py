import re

erro = ""
try:
    nome = input("Digite o seu nome: ")
    if re.search("\d", nome):
        erro = "Erro: o seu nome deve possuir apenas letras."
        raise ValueError
    telefone = input("Digite o seu número de telefone: ")
    if not re.search("\d{2} \d{5}-\d{4}", telefone):
        erro = "Erro: o seu número de telefone está inválido"
        raise ValueError
    print(f"Nome: {nome}\nTelefone: {telefone}")
except ValueError:
    print(erro)

finally:
    print("Fim do programa.")