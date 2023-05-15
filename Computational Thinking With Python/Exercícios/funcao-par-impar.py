numero = 1
print("Digite zero para finalizar")

def par_impar(numero):
    if numero%2 == 0:
            print("Este número é par")
    else:
        print("Este número é ímpar")

while numero != 0:
        numero = int(input("Digite o número desejado: "))
        par_impar(numero)
