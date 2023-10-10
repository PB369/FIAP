import random
import re

nomes_funcionario = ("Guilherme", "Pedro", "Rodrigo", "Vinícius")

def sorteio_nome(nomes_funcionario):
    sorteio = random.randint(0, 3)
    funcionario = nomes_funcionario[sorteio]

    return funcionario


vinhos = {
    1: {"Nome": "Vinho Suave Tinto", "Preço": 15, "Estoque": 25},
    2: {"Nome": "Vinho Seco Tinto", "Preço": 25, "Estoque": 40},
    3: {"Nome": "Vinho Suave Branco", "Preço": 35, "Estoque": 0},
    4: {"Nome": "Vinho Seco Branco", "Preço": 30, "Estoque": 27},
    5: {"Nome": "Vinho Sem Álcool", "Preço": 40, "Estoque": 20}
}

try:
    print(f"Seja bem-vindo à Vinheria Agnello! Eu sou o {sorteio_nome(nomes_funcionario)} e irei te acompanhar na sua compra.")

    verificar = True

    dados_cliente = {
        "Nome": "",
        "CEP": "",
        "Ano de Nascimento": ""
    }

    def verificar():
        cliente = input("\nPara começarmos, qual é o seu nome?\n")
        while not re.search("\w" and "\D", cliente):
            cliente = input("Você errou o seu nome. Digite ele novamente, por favor (apenas caracteres são aceitos): ")
            dados_cliente.update({"Nome": cliente})
        dados_cliente.update({"Nome": cliente})

        cep_cliente = input("\nE qual é o seu CEP?\n")
        while not re.search("\d{5}-\d{3}", cep_cliente):
            cep_cliente = input("Seu CEP está errado. Digite ele novamente, por favor (no formato completo): ")
            dados_cliente.update({"CEP": cep_cliente})
        dados_cliente.update({"CEP": cep_cliente})

        nasc_cliente = input("\nEm que ano você nasceu?\n")
        while not re.search("\d{4}", nasc_cliente):
            nasc_cliente = input("Você escreveu seu ano de nascimento errado. Informe-o novamente, mas apenas com os quatro dígitos: ")
        dados_cliente.update({"Ano de Nascimento": nasc_cliente})

        if(2023 - int(dados_cliente["Ano de Nascimento"])) < 18:
            print("\nInfelizmente você não pode comprar vinhos, pois és menor de idade.")
            raise ValueError

    verificar()

    print("\nEstas são as opções da casa:\n")
    num = 0
    for i in vinhos:
        num += 1
        if vinhos[i]["Estoque"] > 0:
            print(f"({num}) {vinhos[i]['Nome']} \t R${vinhos[i]['Preço']:.2f}")

    escolha_vinho = int(input("\nEscolha um dos vinhos acima, pelo seu número indicado: "))
    while not(escolha_vinho > 0 and escolha_vinho !=3):
        escolha_vinho = int(input("Esta escolha não existe. Digite outra opção: "))

    condicao = True
    while condicao == True:
        escolha_quantidade = int(input("Quantas garrafas você quer comprar?\n"))
        if escolha_quantidade > vinhos[escolha_vinho]["Estoque"]:
            print("Infelizmente não temos esta quantidade no estoque, escolha uma quantia menor.\n")
        else:
            condicao = False

    vinhos[escolha_vinho].update({f"Estoque": vinhos[escolha_vinho]["Estoque"] - escolha_quantidade})

    subtotal = escolha_quantidade * vinhos[escolha_vinho]["Preço"]

    dados_compra = [vinhos[escolha_vinho]["Nome"], vinhos[escolha_vinho]["Preço"], escolha_quantidade, subtotal]

    print(f"""
{dados_cliente['Nome']}, foi um prazer atendê-lo. Segue abaixo as informações da sua compra:

Item Comprado\t\tPreço\t\tQuantidade\t\tSubtotal
{dados_compra[0]}\tR${dados_compra[1]:.2f}\t\t{dados_compra[2]}\t\t\t{dados_compra[3]}
""")
    
    print("Nosso estoque após esta compra ficou assim:\n")
    for i in vinhos:
        print(f"{vinhos[i]['Nome']}\tPreço: R${vinhos[i]['Preço']:.2f}\tEstoque: {vinhos[i]['Estoque']}")

except ValueError:
    print("Volte um outro dia!")