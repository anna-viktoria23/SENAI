#-*- coding: UTF-8 -*-

print("Me de três valores e lhe informarei se eles podem ou não formar os lados de um triângulo e qual tipo de triângulo seria: equilátero, isósceles ou escaleno.")

n1= float(input("Digite o primeiro valor: "))
n2= float(input("Digite o segundo valor: "))
n3= float(input("Digite o terceiro valor: "))

num1= n1+n2
num2= n2+n3
num3= n3+n2

if num1 < n3 and num2 < n1 and num3 < n2:
    print("Os números não podem formar um triangulo")
if n1==n2==n3 or n2==n3==n1 or n3==n1==n2:
    print("o triangulo é equilátero")
elif n1!=n2==n3 or n2!=n3==n2 or n3!=n1==n2:
    print("O triangulo é isósceles")
elif n1!=n2!=n3 or n2!=n3!=n1 or n3!=n1!=n2:
    print("O triangulo é escaleno")
