# -*- coding: UTF-8 -*-

print("Olá usuário! Eu irei lhe apresentar os números divisiorios do número que você desejar :P")

val= int(input("Digite o número desejado: "))

for i in range(1, val+1,1):
    if val % i == 0:
        print(i)
