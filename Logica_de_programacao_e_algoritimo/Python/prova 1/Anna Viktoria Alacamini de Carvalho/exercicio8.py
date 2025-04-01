#Questão 8

#-*- coding: UTF-8 -*-

print("Olá usuário! Neste programa eu irei te informar se o número é negativo ou positivo")

n1= int(input("Digite o seu valor: "))

while True:
    if n1 >= 0:
        print("Seu número é positivo")
    elif n1 <= 0:
        print("Seu número é negativo")
    else:
        print("Alguma coisa deu errado. Por favor, reinicie seu programa")
    break
      
