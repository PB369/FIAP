# RM97937 - Pedro Henrique Fernandes Lô de Barros

ditado = input("Digite um ditado popular: ")
arquivo = open("texto-ditado.txt", "w", encoding="utf-8")
arquivo.write(ditado)
arquivo.close()
arquivo = open("texto-ditado.txt", "r", encoding="utf-8")
print(arquivo.read())
arquivo.close()