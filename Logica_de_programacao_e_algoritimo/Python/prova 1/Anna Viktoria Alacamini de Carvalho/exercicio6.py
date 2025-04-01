#Questão 6

#-*- coding: UTF-8 -*-

print("""Olá usuário, neste programa eu irei te mostrar todos os numeros que são mutiplos
de 5 até o número que você quiser""")

num= int(input("Digite o número desejado: "))

for i in range(0, num+1, 5):
    print(i)
