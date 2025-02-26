#Recebendo a escolha do usuário:
i = int(input(
"""Digite 1 para a área do quadrado
Digite 2 para a área do retângulo
Digite 3 para a área do triângulo
Digite 4 para a área do trapézio

-> """
))

#Calculando e exibindo a área do polígono selecionado:
match i:
    case 1:
        a = float(input("Digite o valor de um dos lados: "))
        print(f"A área do quadrado é {(a*a):.2f}")
    case 2:
        a = float(input("Digite o valor da altura: "))
        b = float(input("Digite o valor da base: "))
        print(f"A área do retângulo é {(a*b):.2f}")
    case 3:
        a = float(input("Digite o valor da altura: "))
        b = float(input("Digite o valor da base: "))
        print(f"A área do triângulo é {((a*b)/2):.2f}")
    case 4:
        a = float(input("Digite o valor da base maior: "))
        b = float(input("Digite o valor da base menor: "))
        c = float(input("Digite o valor da altura: "))
        print(f"A área do trapézio é {(((a*b)*c)/2):.2f}")
    case _: #Caso o usuário digite um valor indesejado
        print("Você inseriu um número inválido. Tente novamente.")
    