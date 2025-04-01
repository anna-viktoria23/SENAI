# -*- coding: UTF-8 -*-

print("Olá usuário! neste programa você me dará um valor e eu lhe direi se ele é primo ou não :)")

n1= int(input("digite o valor para conferir: "))

def primo (n1):
    for i in range (1,n1):
        if n1 % i == 0:
            print ("O número não é primo")
        return
    else:
        print("O numero é primo")

primo (n1)
