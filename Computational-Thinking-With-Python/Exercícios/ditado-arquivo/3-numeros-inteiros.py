# RM97937 - Pedro Henrique Fernandes Lô de Barros

try:
  condicao = 1
  conjunto_num = {"definindo o set"}
  while not condicao == 0:
    num =int(input("Digite um número inteiro (digite zero para parar): "))
    if num != 0:
      conjunto_num.add(num)
      conjunto_num.discard("definindo o set")
    else:
      condicao = num
  arquivo_conjunto = open("numeros.txt", "w")
  for i in conjunto_num:
    if i%2 == 0:
      arquivo_conjunto.write(f"{i}\n")
  arquivo_conjunto.close()
  arquivo_conjunto = open("numeros.txt", "r", encoding="utf-8")
  print(arquivo_conjunto.read())
except ValueError:
  print("Só são aceitos números inteiros.")