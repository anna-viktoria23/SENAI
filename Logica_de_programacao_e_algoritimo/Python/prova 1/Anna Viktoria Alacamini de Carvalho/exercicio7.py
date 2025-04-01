#Questão 7

#-*- coding: UTF-8 -*-

print("""Olá usuário! Neste programa irei lhe dar o resutado da potência que você quiser.
      só preciso que você me de os valores desejados :)""")

num1= int(input("Digite o valor (Essa será sua base):  "))
num2= int(input("Digite o valor (Essa será sua potência: "))
expoente= num1 ** num2

def potencia(num1, num2):
    global expoente
    return(expoente)

potencia(num1, num2)
print("O resultado da sua potência foi de: :)", expoente)
    
