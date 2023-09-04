# RM97937 - Pedro Henrique Fernandes Lô de Barros

novo_ditado = input("Digite um novo ditado popular: ")
arquivo = open("texto-ditado.txt", "a", encoding="utf-8")
arquivo.write(f"\n{novo_ditado}")
arquivo.close()
arquivo = open("texto-ditado.txt", "r", encoding="utf-8")
print(arquivo.read())
arquivo.close()