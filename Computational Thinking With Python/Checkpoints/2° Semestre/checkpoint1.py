import random
import re

nomes_funcionario = ("Guilherme", "Pedro", "Rodrigo", "Vinícius")

def sorteio_nome(nomes_funcionario):
    sorteio = random.randint(0, 3)
    funcionario = nomes_funcionario[sorteio]

    return funcionario


vinhos = {
    "Vinho Suave Tinto": {"Preço": 15, "Estoque": 25},
    "Vinho Seco Tinto": {"Preço": 25, "Estoque": 40},
    "Vinho Suave Branco": {"Preco": 35, "Estoque": 0},
    "Vinho Seco Branco": {"Preço": 30, "Estoque": 27},
    "Vinho Sem Álcool": {"Preço": 40, "Estoque": 20}
}

try:
    print(f"Seja bem-vindo à Vinheria Agnello! Eu sou o {sorteio_nome(nomes_funcionario)} e irei te acompanhar na sua compra.")

    cliente = input("Para começarmos, me diga o seu nome: ")
    cep_cliente = input("\nE qual é o seu CEP?\n")
    nasc_cliente = input("\nEm que ano você nasceu?\n")

    verificar = True

    dados_cliente = {
        "Nome": cliente,
        "CEP": cep_cliente,
        "Ano de Nascimento": nasc_cliente
    }

    def verificar():
        while not re.search("\w", dados_cliente["Nome"]):
            cliente = input("Você errou o seu nome. Digite ele novamente, por favor (apenas caracteres são aceitos): ")
            dados_cliente.update({"Nome": cliente})

        while not re.search("\d{5}-\d{3}", dados_cliente["CEP"]):
            cep_cliente = input("Seu CEP está errado. Digite ele novamente, por favor (no formato completo): ")
            dados_cliente.update({"CEP": cep_cliente})

        while not re.search("\d{4}", dados_cliente["Ano de Nascimento"]):
            nasc_cliente = input("Você escreveu seu ano de nascimento errado. Informe-o novamente, mas apenas com os quatro dígitos: ")
            dados_cliente.update({"Ano de Nascimento": nasc_cliente})

        if(2023 - int(dados_cliente["Ano de Nascimento"])) < 18:
            print("\nInfelizmente você não pode comprar vinhos, pois és menor de idade.")
            raise ValueError

    verificar()
    num = 1
    for i in vinhos:
        if vinhos[i]["Estoque"] > 0:
            print(f"({num}) {i} \t R${vinhos[i]['Preço']:.2f}")
            num += 1

    escolha_vinho = int(input("Escolha um dos vinhos acima, pelo seu número indicado: "))

    escolha_quantidade = 0
    while escolha_quantidade <= vinhos[i]["Estoque"]:
        escolha_quantidade = int(input("Quantas garrafas você quer comprar?\n"))

except ValueError:
    print("Volte um outro dia!")