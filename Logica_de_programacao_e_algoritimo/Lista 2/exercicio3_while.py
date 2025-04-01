# -*- coding: UTF-8 -*-

print("Olá usuário! me de varias idades e eu lhe direi quantas são maiores de 50 e quantas são menores de 21 ;)")

n21 = 0
n50 = 0

while True:
    n1= int(input("Digite a idade: "))
    if n1 == -99:
        print("Você escolheu sair, tchau! ;)")
        break
    if n1 < 21:
        n21 += 1
    elif n1 > 50:
        n50 = n50 + 1
print("A quantidade de pessoas menores de 21 é de: ", n21, " e a quantidade de pessoas maiores que 50 é de: ", n50)
    

