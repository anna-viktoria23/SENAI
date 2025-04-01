# -*- coding: UTF-8 -*-

print("Olá usuário!!!!! Neste programa eu irei fazer a contagem regressiva para você e no final lhe darei uma mensagem de celebração ;)")

n1= int(input("Digite o valor em que começa sua contagem: "))

def cont_regre (n1):
    for i in range (n1,-1,-1):
        print(i)
cont_regre (n1)
print("Feliz ano novo!!!!!")
