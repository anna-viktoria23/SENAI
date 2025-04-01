# -*- coding: UTF-8 -*-

print ("Olá usuário! Digite os valores que quiser e no final irei te mostrar o maior e o menor valor :)")

n1= float(input("Digite o valor desejado: "))
maior= n1
menor= n1

while n1 >= 0:
    n1= float(input("Digite um valor: "))
    if n1 < 0:
        break
    elif n1 < menor:
        menor = n1
    elif n > maior:
        maior = n1
print("O maior numero é: ", maior)
print("O menor numero é: ", menor)
