# -*- coding: UTF-8 -*-

print("Olá usuario! me deos valores que eu irei lhe informar a média deles.")

c = 0
a = 0

while True:
    v= int(input("Digite seus valores ou um numero negativo para sair: "))
    if v <=0:
        print("Você escolheu sair :(")
        break
    a = a + v
    c = c + 1
    media= a/c

print("A média dos números digitados foi de: ", media)
