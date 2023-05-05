import random

vinho1 = "Vinho Tinto"
vinho2 = "Vinho Branco"
vinho3 = "Vinho Rosé"
vinho4 = "Espumante"
vinho5 = "Vinho Licoroso"

vinho1_subtotal = vinho2_subtotal = vinho3_subtotal = vinho4_subtotal = vinho5_subtotal = 0

continuar = "sim"
valor_compra = 0
preco_vinho = 0
tipo_vinho = 0
frete = 35


# Determinando qual será o atendente:
atendente = random.randint(1, 4)
match atendente:
    case 1:
        atendente = "Guilherme"
    case 2:
        atendente = "Pedro"
    case 3:
        atendente = "Ricardo"
    case 4:
        atendente = "Vinícius"


print("Bem-vindo a loja virtual da Vinheria Agnello!\n")
# Soliciando os dados necessários do cliente:
cliente = input("Qual é o seu nome?\n")
print(f"Olá, {cliente}. Eu sou o {atendente} e irei te acompanhar na sua visita a nossa loja. Mas antes eu preciso saber, quantos anos você têm?\n")
idade = int(input())

# Verificando se o cliente é maior de idade:
if idade < 18:
    print(f"{cliente}, sinto em lhe informar que não podemos lhe vender bebidas alcóolicas. Volte quando você tiver 18 anos. ")
else:
    cep = input("Que bom saber! E qual é o seu CEP?\n")
    # Exibindo as opções de compra:
    print("\nMuito bem. Tendo essas informações, agora eu vou lhe mostrar as opções da casa. Veja abaixo a lista de vinhos que possuímos:")
    print("""
    [0] - Cancelar Compra
    [1] - Vinho Tinto\t | R$75,00 
    [2] - Vinho Branco\t | R$105,00
    [3] - Vinho Rosé\t | R$140,00
    [4] - Espumante\t | R$350,00
    [5] - Vinho Licoros\t | R$410,00
    """)
    # Criando um loop para permitir a adição de mais itens da compra no carrinho:
    while (continuar.lower().strip() != "não" and continuar != "0") or tipo_vinho > 0:
        if continuar == "sim":
            tipo_vinho = int(input("\nQual tipo de vinho você deseja adquirir? (Digite o número de um vinho por vez)\n"))

            if tipo_vinho > 0 and tipo_vinho <=5:
                quantidade = int(input("\nE quantas garrafas você deseja para a sua escolha?\n"))
                if quantidade < 1:
                    print("Desculpe, mas a quantidade que você pediu não faz sentido. Você precisa ao menos selecionar uma garrafa de vinho.")
                else:

                    if tipo_vinho == 1:
                        vinho1 = True
                        preco_vinho = 75
                        vinho1_subtotal += (preco_vinho * quantidade)
                    elif tipo_vinho == 2:
                        vinho2 = True
                        preco_vinho = 105
                        vinho2_subtotal += (preco_vinho * quantidade)
                    elif tipo_vinho == 3:
                        vinho3 = True
                        preco_vinho = 140
                        vinho3_subtotal += (preco_vinho * quantidade)
                    elif tipo_vinho == 4:
                        vinho4 = True
                        preco_vinho = 350
                        vinho4_subtotal += (preco_vinho * quantidade)
                    elif tipo_vinho == 5:
                        vinho5 = True
                        preco_vinho = 410
                        vinho5_subtotal += (preco_vinho * quantidade)
                    continuar = input("\nVocê deseja continuar comprando? Se você quer cancelar a compra, digite 0.\n").lower().strip()
                    # Verificando se o cliente quer cancelar a compra no momento do continuar:
                    if continuar == "0":
                        print("Muito bem, sua compra foi cancelada. Volte quando quiser!")
                    # Verifiando a validade da resposta do continuar:
                    elif continuar != "sim" and continuar != "não" and continuar != 0:
                        print("Desculpe, não entendi a sua resposta.")
                        continuar = input("\nVocê deseja continuar comprando? Se você quer cancelar a compra, digite 0.\n").lower().strip()
                    tipo_vinho = 0

            # Permitindo ao cliente cancelar a sua compra:
            elif tipo_vinho == 0:
                    print("Muito bem, sua compra foi cancelada. Volte quando quiser!")
                    continuar = "0"
            else:
                print("Desculpe, mas a sua resposta não corresponde às opções disponíveis.")

    # Verificando se o cliente está comprando algum vinho e se ele não cancelou a compra:
    if (tipo_vinho > 0 and tipo_vinho <= 5) or continuar != "0":

        valor_compra = vinho1_subtotal + vinho2_subtotal + vinho3_subtotal + vinho4_subtotal + vinho5_subtotal

        if valor_compra > 200:
            frete = 0

        total = valor_compra + frete

        print(f"\nCerto. Segue abaixo as informações da compra:\n")

        # Exibindo a nota fiscal da compra:
        print(f"Nome do Atendente: {atendente}")
        print(f"Nome do Cliente: {cliente}")

        #
        print("\nItens da Compra:")
        if vinho1 == True:
            vinho1 = "Vinho Tinto"
            print(f"{vinho1} | R$75,00")
            print(f" Subtotal do Produto: R${vinho1_subtotal:.2f}")
        if vinho2 == True:
            vinho2 = "Vinho Branco"
            print(f"{vinho2} | R$105,00")
            print(f" Subtotal do Produto: R${vinho2_subtotal:.2f}")
        if vinho3 == True:
            vinho3 = "Vinho Rosé"
            print(f"{vinho3} | R$140,00")
            print(f" Subtotal do Produto: R${vinho3_subtotal:.2f}")
        if vinho4 == True:
            vinho4 = "Espumante"
            print(f"{vinho4} | R$350,00")
            print(f" Subtotal do Produto: R${vinho4_subtotal:.2f}")
        if vinho5 == True:
            vinho5 ="Vinho Licoroso"
            print(f"{vinho5} | R$410,00")
            print(f" Subtotal do Produto: R${vinho5_subtotal:.2f}")

        print(f"\nSubtotal da Compra: R${valor_compra:.2f}")


        if frete == 0:
            print("Valor do Frete: GRÁTIS")
        else:
            print(f"Valor do Frete: R${frete:.2f}")

        print(f"\nTotal a Pagar: R${total:.2f}")