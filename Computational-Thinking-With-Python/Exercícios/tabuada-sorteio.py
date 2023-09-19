import random

#Sorteando um número inteiro de 2 até 9:
num = random.randint(2, 9)

#Verificando se este número é maior ou menor do que cinco e imprimindo sua tabuada em ordem crescente ou decrescente:
if num <= 5:
    print(f"A tabuada de {num} em ordem crescente é:")
    print(num, "x", 1, "=", num*1)
    print(num, "x", 2, "=", num*2)
    print(num, "x", 3, "=", num*3)
    print(num, "x", 4, "=", num*4)
    print(num, "x", 5, "=", num*5)
    print(num, "x", 6, "=", num*6)
    print(num, "x", 7, "=", num*7)
    print(num, "x", 8, "=", num*8)
    print(num, "x", 9, "=", num*9)
    print(num, "x", 10, "=", num*10)
else:
    print(f"A tabuada de {num} em ordem decrescente é:")
    print(num, "x", 10, "=", num*10)
    print(num, "x", 9, "=", num*9)
    print(num, "x", 8, "=", num*8)
    print(num, "x", 7, "=", num*7)
    print(num, "x", 6, "=", num*6)
    print(num, "x", 5, "=", num*5)
    print(num, "x", 4, "=", num*4)
    print(num, "x", 3, "=", num*3)
    print(num, "x", 2, "=", num*2)
    print(num, "x", 1, "=", num*1)