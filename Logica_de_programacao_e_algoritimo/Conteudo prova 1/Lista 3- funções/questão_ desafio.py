# -*- coding: UTF-8 -*-

print("Olá usuário! me de um número que eu irei lhe dizer quantos digitos ele tem :)")

n1= int(input("Digite o numero desejado: "))
cont= 0

def contagem (n1):
    global cont
    while n1 >= 1:
        n1= n1/10
        cont += 1

contagem (n1)
print("A quantidade de digitos que este valor tem é de: ", cont)
