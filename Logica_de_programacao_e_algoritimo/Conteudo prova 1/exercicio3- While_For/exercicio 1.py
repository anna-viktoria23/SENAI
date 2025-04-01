# -*- coding: UTF-8 -*-

print("Olá usuário! me de o valor de os valores dejesados que eu irei lhe dar o triplo de cada número, e quando você digitar -999, você estara escolhendo sair do programa")

valor = 0
while True:
    valor= int(input("digite o valor desejado, ou -999 para sair: "))
    if valor == -999:
        print("Você escolheu sair :(")
        break
    print(valor * 3)
    
    
    
