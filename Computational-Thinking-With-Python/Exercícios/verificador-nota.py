media = float(input("Digite a média de matemática: "))
if media >= 6:
    print("O aluno foi aprovado.")
elif media < 6 and media >= 5:
    print("O aluno está de recuperação.")
else:
    print("O aluno foi reprovado.")