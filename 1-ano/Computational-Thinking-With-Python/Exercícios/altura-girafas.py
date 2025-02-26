#Recebendo as alturas de cada girafa
altura1 = float(input("Digite a altura da girafa 1: "))
altura2 = float(input("Digite a altura da girafa 2: "))
altura3 = float(input("Digite a altura da girafa 3: "))
altura4 = float(input("Digite a altura da girafa 4: "))
altura5 = float(input("Digite a altura da girafa 5: "))

#Comparando as alturas e determinando qual é a de maior valor:
if altura1 > altura2 and altura3 and altura4 and altura5:
    print(f"A maior girafa é a que possui {altura1} de altura.")
elif altura2 > altura5 and altura4 and altura3 and altura2:
    print(f"A maior girafa é a que possui {altura2} de altura.")
elif altura3 > altura4 and altura3 and altura2 and altura1:
    print(f"A maior girafa é a que possui {altura3} de altura.")
elif altura4 > altura3 and altura2 and altura1 and altura5:
    print(f"A maior girafa é a que possui {altura4} de altura.")
elif altura5 > altura2 and altura1 and altura5 and altura4:
    print(f"A maior girafa é a que possui {altura4} de altura.")