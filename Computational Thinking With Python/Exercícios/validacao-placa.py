import re

erro = "A sua placa está inválida"

try:
    placa = input("Digite a sua placa: ")
    if re.search("[A-Z]{3}\d{1}[A-Z]{1}\d{2}", placa):
        print(f"A sua placa é: {placa} e está de acordo com os padrões da MERCOSUL.")
    else:
        raise ValueError
except ValueError:
    print(erro)
finally:
    print("\nPrograma finalizado.")