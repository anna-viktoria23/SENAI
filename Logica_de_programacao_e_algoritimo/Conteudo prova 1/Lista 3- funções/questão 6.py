# -*- coding: UTF-8 -*-

print("Olá usuário! Neste programa eu irei converter a temperatura de Celcius para Fahrenheit, e vice-versa")

temp= str(input("Digite C para converter para celcius ou F para converter para fahrenheit: "))
n1= int(input("Digite a temperatura: "))

conta_f= n1 * 9/5 + 32
conta_c= n1 * 9/5 - 32

def conversão (temp):
    if temp == "C":
        print("O resultado da conversão de celcius para fahrenheit foi de: ", conta_f)
        return
    elif temp == "F":
        print("O resultado da conversão de fahrenheit para celcius foi de: ", conta_c)

conversão (temp)
    
    
