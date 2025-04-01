# -*- coding: UTF-8 -*-

print("Olá usuário! Me de um numero que eu irei fazer o Fatorial dele ;)")

v= int(input("digite o valor: "))
fat= 1

for i in range(v,0,-1):
    fat= i * fat
print("O resultado da fatorial é de: ", fat)
