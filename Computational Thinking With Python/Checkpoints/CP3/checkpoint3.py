import random
import re

verificacao_nome = verificacao_cep = verificacao_ano_nascimento = sub_verificacao_ano_nascimento = True

lista_nome = []
sorteio_nome = random.randint(1, 3)

def nome_funcionario():
    match sorteio_nome:
        case 1:
            lista_nome.append("Guilherme")
        case 2:
            lista_nome.append("Pedro")
        case 3:
            lista_nome.append("Ricardo")
    return lista_nome
nome_funcionario()

def continuar():
    print("\nMuito bem! Suas informações são o suficiente para darmos continuidade à compra. Veja abaixo a lista de vinhos que estamos oferecendo:\n")

    lista_vinhos = ["Espumante | R$350,00", "Vinho Branco | R$105,00", "Vinho Licoroso | R$410,00","Vinho Rosé | R$140,00", "Vinho Tinto | R$75,00 "]

    print(f"{lista_vinhos[0]}")


print(f"Bem-vindo à vinheria Agnello! Você será atendido pelo {lista_nome[0]}.")

nome_cliente = input("\nQual é o seu nome?\n")

while verificacao_nome:
    if re.search("\d", nome_cliente):
        print("Perdão, mas acho que você escreveu seu nome errado. Há números nele...")
        nome_cliente = input("Me informe o seu nome novamente, por favor\n")

    elif nome_cliente == "":
        print("O que você escreveu não tem sentido. Para continuar com o atendimento, eu preciso do seu nome.")
        nome_cliente = input("Me informe o seu nome novamente, por favor\n")

    else:
        verificacao_nome = False

cep = input("E o seu CEP?\n")

while verificacao_cep:
    if not re.search("\d{5}-\d{3}", cep):
        if re.search("[a-z]", cep):
            print("Você escreveu seu CEP com letras.")
            cep = input("Escreva-o novamente, por favor.\n")
        else:
            print("Opa, acho que você escreveu seu CEP da maneira errada.\nLembre-se de que o formato dele é com o tracinho (-) após os cinco primeiros números.")
            cep = input("\nEscreva-o novamente, por favor.\n")

    else:
        verificacao_cep = False

ano_nascimento = input("Por fim, em que ano você nasceu?\n")

while verificacao_ano_nascimento:
    if re.search("\D", ano_nascimento):
        print("Opa, você colocou algo errado na hora da escrita. Verifique o erro e escreva-o novamente.\n")
        ano_nascimento = input()
    else:
        verificacao_ano_nascimento = False

while sub_verificacao_ano_nascimento:
    if len(str(ano_nascimento)) != 4:
        print("Ops, você me informou um ano estranho. Lembre-se de que os anos de nossa época tem quatro dígitos (ou será que você é um viajante do tempo? o-o).")
        ano_nascimento = input("\nEscreva-o novamente, por favor\n")
    else:
        ano_nascimento = int(ano_nascimento)
        if (2023 - ano_nascimento) < 18:
            print("Desculpe, mas não podemos vender nossos produtos a menos de idade. Volte quando você tiver 18 anos.")
            break
        else:
            sub_verificacao_ano_nascimento = False
            continuar()
