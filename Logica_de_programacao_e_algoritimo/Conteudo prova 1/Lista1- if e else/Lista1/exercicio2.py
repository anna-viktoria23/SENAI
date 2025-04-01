#-*- coding: UTF-8 -*-

import math

print("Me de um numero que eu lhe vou fazer a raiz quadrada, caso seja positivo ou igual a zero, ou o quadrado dele, caso ele seja negativo")

n1= int(input("Digite o numero: "))

if n1>=0:
        raiz= math.sqrt(n1)
        print("A raiz quadrada do numero é: ",raiz)
else:
    quadrado= n1*n1
    print("O quadrado do numero é: ",quadrado)
