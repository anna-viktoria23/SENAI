# -*- coding: UTF-8 -*-

print ("Olá usuario. me de o sexo de varias pessoas ue eu te informarei quantas foram do sexo masculino")

cont= 0

for i in range (10):
    s= str (input("Infrome o sexo das pessoas (f, F, m, M): "))
    if s== "m" or s== "M":
        cont= cont + 1
print ("A quantidade de pessoas do sexo masculino fora: ", cont)
        

