# -*- coding: UTF-8 -*-

print("Olá usuário! Neste programa eu irei imprimir a tabela da tabuada do número 1 até o número 10 :)")


num = int(input("Digite um número entre 1 e 10: "))
          
def tabuada (num):
    for i in range (1,11):
        print (f" {num} x {i} = {num*i}")

tabuada(num)
print()
